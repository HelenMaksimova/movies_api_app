from uuid import UUID

from pydantic import BaseModel, ConfigDict

__all__ = (
    "GenreDC",
    "GenreExtendedDC",
)


class GenreDC(BaseModel):
    model_config = ConfigDict(extra="ignore", from_attributes=True)

    id: UUID
    name: str


class GenreExtendedDC(GenreDC):
    description: str | None = None
