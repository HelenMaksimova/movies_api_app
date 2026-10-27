from functools import lru_cache

from elasticsearch import AsyncElasticsearch
from fastapi import Depends
from redis.asyncio import Redis

from src.core.enums import GenreSortEnum
from src.db.elastic import get_elastic
from src.db.redis import get_redis
from src.models.person import PersonDC, PersonExtendedDC
from src.utils import BaseService

__all__ = (
    "PersonService",
    "get_person_service",
)


class PersonService(BaseService[PersonDC, PersonExtendedDC]):
    _base_model = PersonDC
    _extended_model = PersonExtendedDC
    _sort_enum = GenreSortEnum
    _elastic_index = "persons"

    search_field = "name"


@lru_cache()
def get_person_service(
    redis: Redis = Depends(get_redis),
    elastic: AsyncElasticsearch = Depends(get_elastic),
) -> PersonService:
    return PersonService(redis, elastic)
