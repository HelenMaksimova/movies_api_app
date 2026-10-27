from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

__all__ = (
    "PersonDC",
    "PersonExtendedDC",
)


class _PersonFilmRolesDC(BaseModel):
    model_config = ConfigDict(extra="ignore", from_attributes=True)

    id: UUID
    roles: list[str] = Field(default_factory=list)


class PersonDC(BaseModel):
    model_config = ConfigDict(extra="ignore", from_attributes=True)

    id: UUID
    name: str


class PersonExtendedDC(PersonDC):
    films: list[_PersonFilmRolesDC] = Field(default_factory=list)
