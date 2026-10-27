from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from src.models.genre import GenreDC
from src.models.person import PersonDC

__all__ = (
    "FilmDC",
    "FilmExtendedDC",
)


class FilmDC(BaseModel):
    model_config = ConfigDict(extra="ignore", from_attributes=True)

    id: UUID
    title: str
    imdb_rating: float


class FilmExtendedDC(FilmDC):
    description: str | None
    genres: list[GenreDC] = Field(default_factory=list)
    actors: list[PersonDC] = Field(default_factory=list)
    writers: list[PersonDC] = Field(default_factory=list)
    directors: list[PersonDC] = Field(default_factory=list)
    actors_names: list[str] = Field(default_factory=list)
    writers_names: list[str] = Field(default_factory=list)
    directors_names: list[str] = Field(default_factory=list)
