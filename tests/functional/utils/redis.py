from redis import ConnectionError, RedisError
from redis.asyncio import Redis

__all__ = ("clear_cache",)


async def clear_cache(redis_cli: Redis, *keys: str) -> None:
    try:
        if keys:
            await redis_cli.delete(*keys)
        else:
            await redis_cli.flushdb()

    except ConnectionError as err:
        raise ValueError(f"Redis cannot be connected with error: {err}")
    except RedisError as err:
        raise ValueError(f"Redis cannot clear cache with error: {err}")
