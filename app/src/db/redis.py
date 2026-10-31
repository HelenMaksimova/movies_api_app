from logging import getLogger
from typing import TYPE_CHECKING

from fastapi import Request
from redis.asyncio import (
    ConnectionError as RedisConnectionError,
    Redis,
    TimeoutError as RedisTimeoutError,
)

if TYPE_CHECKING:
    from src.core.config import RedisConfigDC

__all__ = (
    "get_client",
    "get_redis",
)


logger = getLogger()


async def get_client(config: "RedisConfigDC") -> Redis | None:
    client = Redis(
        host=config.host,
        port=config.port,
        password=config.password,
        db=config.db,
        decode_responses=config.decode_responses,
        retry_on_error=[RedisConnectionError, RedisTimeoutError],
    )

    try:
        await client.ping()
        logger.info("[Redis] Was connected on: %s:%s", config.host, config.port)
    except (RedisConnectionError, RedisTimeoutError) as err:
        logger.error("[Redis] Was not connected with error: %s", err)

    return client


async def get_redis(request: Request) -> Redis | None:
    return request.app.state.redis
