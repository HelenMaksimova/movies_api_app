from functools import lru_cache

from elasticsearch import AsyncElasticsearch
from fastapi import Depends
from redis.asyncio import Redis

from src.core.enums import FilmSortEnum
from src.db.elastic import get_elastic
from src.db.redis import get_redis
from src.models.film import FilmDC, FilmExtendedDC
from src.services.field_filters import genre_filter, person_films_filter
from src.utils import BaseService

__all__ = (
    "FilmService",
    "get_film_service",
)


class FilmService(BaseService[FilmDC, FilmExtendedDC]):
    _base_model = FilmDC
    _extended_model = FilmExtendedDC
    _sort_enum = FilmSortEnum
    _elastic_index = "movies"

    search_field = "title"
    filters_map = {
        "genre": genre_filter,
        "person_id": person_films_filter,
    }


@lru_cache()
def get_film_service(
    redis: Redis = Depends(get_redis),
    elastic: AsyncElasticsearch = Depends(get_elastic),
) -> FilmService:
    return FilmService(redis, elastic)
