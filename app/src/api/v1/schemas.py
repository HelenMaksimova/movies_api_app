from uuid import UUID

from pydantic import BaseModel, Field, RootModel

from src.core.enums import FilmSortEnum, GenreSortEnum, PersonSortEnum
from src.utils import ListQuerySchema, ListSearchQuerySchema

__all__ = (
    "DetailFilmResponseSchema",
    "DetailGenreResponseSchema",
    "DetailPersonResponseSchema",
    "ListFilmQuerySchema",
    "ListFilmResponseSchema",
    "ListGenreResponseSchema",
    "ListPersonResponseSchema",
    "ListSearchFilmQuerySchema",
    "ListSearchPersonQuerySchema",
)


class ListFilmQuerySchema(ListQuerySchema):
    _sort_enum = FilmSortEnum

    genre: UUID | None = None


class ListGenreQuerySchema(ListQuerySchema):
    _sort_enum = GenreSortEnum


class ListSearchFilmQuerySchema(ListSearchQuerySchema):
    _sort_enum = FilmSortEnum

    genre: UUID | None = None


class ListSearchPersonQuerySchema(ListSearchQuerySchema):
    _sort_enum = PersonSortEnum


class _GenreResponseSchema(BaseModel):
    uuid: UUID = Field(alias="id")
    name: str


class _PersonResponseSchema(BaseModel):
    uuid: UUID = Field(alias="id")
    full_name: str = Field(alias="name")


class _FilmResponseSchema(BaseModel):
    uuid: UUID = Field(alias="id")
    title: str
    imdb_rating: float = 0.0


class _FilmRolesResponseSchema(BaseModel):
    uuid: UUID = Field(alias="id")
    roles: list[str] = Field(default_factory=list)


class DetailFilmResponseSchema(_FilmResponseSchema):
    description: str | None
    genres: list[_GenreResponseSchema] = Field(default_factory=list)
    actors: list[_PersonResponseSchema] = Field(default_factory=list)
    writers: list[_PersonResponseSchema] = Field(default_factory=list)
    directors: list[_PersonResponseSchema] = Field(default_factory=list)


class DetailGenreResponseSchema(_GenreResponseSchema):
    description: str | None


class DetailPersonResponseSchema(_PersonResponseSchema):
    films: list[_FilmRolesResponseSchema] = Field(default_factory=list)


class ListFilmResponseSchema(RootModel[list[_FilmResponseSchema]]):
    pass


class ListPersonResponseSchema(RootModel[list[DetailPersonResponseSchema]]):
    pass


class ListGenreResponseSchema(RootModel[list[DetailGenreResponseSchema]]):
    pass
