from collections.abc import Callable
from typing import TYPE_CHECKING, Any, ClassVar, Optional
from uuid import UUID

from backoff import expo, on_exception, random_jitter
from elastic_transport import ObjectApiResponse
from elasticsearch import (
    AsyncElasticsearch,
    ConnectionError as ElasticConnectionError,
    ConnectionTimeout as ElasticTimeoutError,
    NotFoundError,
)
from fastapi import HTTPException
from pydantic import BaseModel
from redis.asyncio import Redis

from src.utils.decorators import async_redis_cache

if TYPE_CHECKING:
    from src.utils.enums import SortEnum

__all__ = ("BaseService",)


class BaseService[BaseServiceModel: BaseModel, ExtendedServiceModel: BaseModel]:
    """Базовый сервис, работающий с Redis и Elasticsearch.
    Реализует базовые методы получения из Elasticsearch
    объекта по идентификатору и списка объектов с сортировкой и фильтрацией"""

    _base_model: BaseServiceModel | None = None
    _extended_model: ExtendedServiceModel | None = None
    _sort_enum: Optional["SortEnum"] = None
    _elastic_index: str | None = None

    search_field: str = "title"
    filters_map: ClassVar[dict[str, Callable]] = {}

    def __init__(self, redis: Redis, elastic: AsyncElasticsearch) -> None:
        self.redis = redis
        self.elastic = elastic

    @property
    def base_model(self) -> type[BaseServiceModel]:
        if self._base_model:
            return self._base_model

        raise ValueError(f"[{self.__class__.__name__}] Base model was not set")

    @property
    def extended_model(self) -> type[ExtendedServiceModel]:
        if self._extended_model:
            return self._extended_model

        raise ValueError(
            f"[{self.__class__.__name__}] Extended model was not set"
        )

    @property
    def elastic_index(self) -> str:
        if self._elastic_index:
            return self._elastic_index

        raise ValueError(
            f"[{self.__class__.__name__}] Elastic index was not set"
        )

    @property
    def sort_enum(self) -> "SortEnum":
        if self._sort_enum:
            return self._sort_enum

        raise ValueError(f"[{self.__class__.__name__}] Sort enum was not set")

    def _get_filters(self, **filters: Any) -> list[dict]:
        """Метод для формирования общего списка выражений для добавления
        фильтрации в запрос к Elasticsearch"""

        results = []

        for filter_name, filter_value in filters.items():
            filter_condition = self.filters_map.get(filter_name)
            if filter_condition:
                results.append(filter_condition(filter_value))

        return results

    def _get_filter_conditions(self, **filters: Any) -> tuple[list[dict], ...]:
        """Метод для формирования списка выражений для добавления
        фильтрации в запрос к Elasticsearch и
        разделения выражений по полям запроса should и filter"""

        should_conditions = []
        filter_conditions = []

        for condition in self._get_filters(**filters):
            if condition_value := condition.get("should"):
                if isinstance(condition_value, (list, tuple, set)):
                    should_conditions.extend(condition_value)
                else:
                    should_conditions.append(condition_value)
            elif condition_value := condition.get("filter"):
                if isinstance(condition_value, (list, tuple, set)):
                    filter_conditions.extend(condition_value)
                else:
                    filter_conditions.append(condition_value)

        return should_conditions, filter_conditions

    def _get_search_condition(self, search_query: str) -> dict:
        """Метод для получения выражения для контекстного поиска по полю"""

        return {"match": {self.search_field: search_query}}

    def _get_elastic_search_query(
        self,
        limit: int = 50,
        offset: int = 0,
        sort: str | None = None,
        search_query: str | None = None,
        **filters,
    ) -> dict:
        """Метод для формирования запроса в Elasticsearch c учётом
        контекстного поиска, фильтрации, сортировки и пагинации"""

        query = {
            "query": {"match_all": {}},
            "from": offset,
            "size": limit,
        }

        cleared_filters = {
            key: value for key, value in filters.items() if value is not None
        }

        if cleared_filters or search_query:
            query["query"].pop("match_all")
            query["query"] = {"bool": {}}

            if cleared_filters:
                should_conditions, filter_conditions = (
                    self._get_filter_conditions(**cleared_filters)
                )

                if should_conditions:
                    query["query"]["bool"]["should"] = should_conditions
                    query["query"]["bool"]["minimum_should_match"] = 1

                if filter_conditions:
                    query["query"]["bool"]["filter"] = filter_conditions

            if search_query:
                query["query"]["bool"]["must"] = self._get_search_condition(
                    search_query
                )

        query["sort"] = self.sort_enum.get_field_by_name(sort).sort_value

        return query

    @on_exception(
        expo,
        (ElasticConnectionError, ElasticTimeoutError),
        max_tries=3,
        jitter=random_jitter,
    )
    async def _elastic_get(self, index: str, id: UUID) -> ObjectApiResponse:
        return await self.elastic.get(index=index, id=str(id))

    @on_exception(
        expo,
        (ElasticConnectionError, ElasticTimeoutError),
        max_tries=3,
        jitter=random_jitter,
    )
    async def _elastic_search(
        self, index: str, query: dict
    ) -> ObjectApiResponse:
        return await self.elastic.search(index=index, body=query)

    async def _get_item_from_elastic(
        self, id: UUID
    ) -> ExtendedServiceModel | None:
        """Внутренний метод для получения из Elasticsearch
        объекта по идентификатору"""

        try:
            doc = await self._elastic_get(self.elastic_index, id)
        except NotFoundError:
            return None
        except ElasticConnectionError:
            raise HTTPException(503, "[Elastic] Connection error")
        except ElasticTimeoutError:
            raise HTTPException(504, "[Elastic] Timeout error")

        return self.extended_model(**doc["_source"])

    async def _get_list_from_elastic(
        self, query: dict, is_extended: bool = False
    ) -> list[BaseServiceModel | ExtendedServiceModel]:
        """Внутренний метод для получения из Elasticsearch
        списка объектов по запросу в виде словаря"""
        try:
            result = await self._elastic_search(self.elastic_index, query)
        except ElasticConnectionError as err:
            raise HTTPException(503, "[Elastic] Connection error") from err
        except ElasticTimeoutError as err:
            raise HTTPException(504, "[Elastic] Timeout error") from err

        if is_extended:
            return [
                self.extended_model(**item["_source"])
                for item in result["hits"]["hits"]
            ]

        return [
            self.base_model(**item["_source"])
            for item in result["hits"]["hits"]
        ]

    @async_redis_cache(60 * 5)
    async def get_item(self, id: UUID) -> ExtendedServiceModel | None:
        """Публичный метод для получения из Elasticsearch
        объекта по идентификатору. Кешируется в Redis"""

        return await self._get_item_from_elastic(id)

    @async_redis_cache(60 * 5)
    async def get_list(
        self,
        page_number: int = 1,
        page_size: int = 50,
        sort: str | None = None,
        search_query: str | None = None,
        is_extended: bool = False,
        **filters: Any,
    ) -> list[BaseServiceModel | ExtendedServiceModel]:
        """Публичный метод для получения из Elasticsearch списка объектов
        c учётом контекстного поиска, фильтрации, сортировки и пагинации.
        Кешируется в Redis"""

        offset = page_size * (page_number - 1)
        query = self._get_elastic_search_query(
            page_size,
            offset,
            sort=sort,
            search_query=search_query,
            **filters,
        )
        return await self._get_list_from_elastic(query, is_extended)
