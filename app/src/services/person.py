from functools import lru_cache

from fastapi import Request

from src.core.enums import GenreSortEnum
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


@lru_cache
def _make_person_service(redis, elastic) -> PersonService:
    return PersonService(redis, elastic)


def get_person_service(request: Request) -> PersonService:
    return _make_person_service(
        request.app.state.redis,
        request.app.state.elastic,
    )
