from functools import lru_cache

from fastapi import Request

from src.core.enums import GenreSortEnum
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


@lru_cache
def _make_genre_service(redis, elastic) -> GenreService:
    return GenreService(redis, elastic)


def get_genre_service(request: Request) -> GenreService:
    return _make_genre_service(
        request.app.state.redis,
        request.app.state.elastic,
    )
