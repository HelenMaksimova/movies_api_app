from typing import ClassVar

from pydantic import BaseModel, Field, field_validator

from src.utils.enums import SortEnum

__all__ = (
    "ListQuerySchema",
    "ListSearchQuerySchema",
)


class ListQuerySchema(BaseModel):
    _sort_enum: ClassVar[type[SortEnum]] = SortEnum

    page_number: int = Field(1, gt=0)
    page_size: int = Field(50, gt=0, le=100)
    sort: str | None = None

    @classmethod
    @property
    def sort_enum(cls) -> type[SortEnum]:
        return cls._sort_enum

    @field_validator("sort")
    @classmethod
    def validate_sort(cls, value: str) -> str:
        if value and value not in cls.sort_enum.names:
            raise ValueError(
                f"Sort must be one of: {sorted(cls.sort_enum.names)}"
            )
        return value


class ListSearchQuerySchema(ListQuerySchema):
    query: str | None = None
