from functools import lru_cache

from elasticsearch import AsyncElasticsearch
from fastapi import Depends
from redis.asyncio import Redis

from src.core.enums import GenreSortEnum
from src.db.elastic import get_elastic
from src.db.redis import get_redis
from src.models.genre import GenreDC, GenreExtendedDC
from src.utils import BaseService

__all__ = (
    "GenreService",
    "get_genre_service",
)


class GenreService(BaseService[GenreDC, GenreDC]):
    _base_model = GenreDC
    _extended_model = GenreExtendedDC
    _sort_enum = GenreSortEnum
    _elastic_index = "genres"

    search_field = "name"


@lru_cache()
def get_genre_service(
    redis: Redis = Depends(get_redis),
    elastic: AsyncElasticsearch = Depends(get_elastic),
) -> GenreService:
    return GenreService(redis, elastic)
