import json
from collections.abc import Callable
from functools import wraps
from hashlib import sha1
from logging import getLogger
from typing import TYPE_CHECKING, Any, ParamSpec, TypeVar

from redis import (
    ConnectionError as RedisConnectionError,
    TimeoutError as RedisTimeoutError,
)

if TYPE_CHECKING:
    from src.utils import BaseService

__all__ = ("async_redis_cache",)

_P = ParamSpec("_P")
_T = TypeVar("_T")


logger = getLogger()


class async_redis_cache:
    """Декоратор для кеширования результата выполнения метода в Redis.
    Ключ для записи - хеш от имени класса-сервиса, метода и
    переданных параметров"""

    def __init__(self, ttl: int = 60 * 5) -> None:
        self.ttl = ttl

    def __call__(self, method: Callable[_P, _T]) -> Callable[_P, _T]:
        @wraps(method)
        async def async_wrapper(
            service: "BaseService", *args: _P.args, **kwargs: _P.kwargs
        ) -> Any:
            key = self._gen_key(service, method, *args, **kwargs)
            result = None

            try:
                if service.redis:
                    result = await service.redis.get(key)

                if result is None:
                    result = await method(service, *args, **kwargs)

                    if service.redis and result is not None:
                        if isinstance(result, (list, tuple)):
                            cache = json.dumps(
                                [item.model_dump_json() for item in result]
                            )
                        else:
                            cache = result.model_dump_json()

                        await service.redis.set(key, cache, self.ttl)
                else:
                    result = json.loads(result)
                    if isinstance(result, (list, tuple)):
                        result = [json.loads(item) for item in result]
            except (RedisConnectionError, RedisTimeoutError):
                logger.error(
                    "[Redis] Connection or timeout error. Cache cannot be set or get"
                )
                result = await method(service, *args, **kwargs)

            return result

        return async_wrapper

    def _gen_key(
        self,
        service: "BaseService",
        method: Callable[_P, _T],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> str:
        return sha1(
            (
                service.__class__.__name__
                + method.__name__
                + str(args)
                + str(kwargs)
            ).encode()
        ).hexdigest()
