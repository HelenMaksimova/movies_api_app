from collections.abc import Iterable
from typing import Any

__all__ = ("get_errors",)


def get_errors(results: Iterable[Any]) -> list[Exception]:
    return [result for result in results if isinstance(result, Exception)]
