from enum import Enum
from typing import TypeVar

from pydantic.dataclasses import dataclass

_SortField = TypeVar("_SortField")

__all__ = (
    "ElasticSortField",
    "SortEnum",
    "SortField",
)


@dataclass
class SortField:
    """Класс поля класса-сортировки. Содержит поля:
    name - имя сортировки, указываемое в квери-параметрах http запросов;
    sort_value - выражение для параметра сортировки в запросах в базы данных;
    alias - название поля для запросов в базы данных,
        если есть отличие от названия в квери-параметрах
    """

    name: str
    sort_value: dict | str | None = None
    alias: str | None = None

    def __post_init__(self) -> None:
        if not self.sort_value:
            self.sort_value = self._construct_sort_value()

    def _construct_sort_value(self) -> str:
        if self.alias:
            return self.alias

        return self.name


class SortEnum(Enum):
    """Класс для работы с сортировками"""

    @classmethod
    def get_field_by_name(cls, name: str) -> _SortField:
        try:
            for field in cls:
                if name == field.value.name:
                    return field.value
            return cls["default"].value
        except KeyError:
            raise ValueError(
                f"Invalid sort name: {name} and default sort is not set"
            )

    @classmethod
    @property
    def names(cls) -> set[str]:
        return {field.value.name for field in cls}


@dataclass
class ElasticSortField(SortField):
    def _construct_sort_value(self) -> dict:
        order = "desc" if self.name.startswith("-") else "asc"
        field_name = (
            self.alias.lstrip("-") if self.alias else self.name.lstrip("-")
        )
        return {field_name: {"order": order}}
