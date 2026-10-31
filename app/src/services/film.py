from collections.abc import Callable
from functools import lru_cache
from typing import ClassVar

from fastapi import Request

from src.core.enums import FilmSortEnum
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
    filters_map: ClassVar[dict[str, Callable]] = {
        "genre": genre_filter,
        "person_id": person_films_filter,
    }


@lru_cache
def _make_film_service(redis, elastic) -> FilmService:
    return FilmService(redis, elastic)


def get_film_service(request: Request) -> FilmService:
    return _make_film_service(
        request.app.state.redis,
        request.app.state.elastic,
    )
