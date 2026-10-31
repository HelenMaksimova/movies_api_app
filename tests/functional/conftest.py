from asyncio import gather
from collections.abc import AsyncGenerator
from logging import config as log_config, getLogger
from pathlib import Path
from typing import Any

from elasticsearch import (
    AsyncElasticsearch,
    ConnectionError as ElasticConnectionError,
)
from pytest import fixture
from pytest_asyncio import fixture as async_fixture
from redis import ConnectionError as RedisConnectionError, RedisError
from redis.asyncio import Redis
from settings import LOG_SETTINGS, test_config
from utils.base import TestBase
from utils.common import get_errors
from utils.elastic import create_index

log_config.dictConfig(LOG_SETTINGS)
logger = getLogger("tests")


@fixture(scope="class", autouse=True)
async def auto_close_session(request):
    """Автоматически закрывает сессию после всех тестов класса"""
    cls = request.cls
    yield
    if issubclass(cls, TestBase):
        await cls._session_close()
        logger.info("[%s] Aiohttp session was closed", cls.__name__)


@async_fixture(scope="session")
async def redis_cli() -> AsyncGenerator[Redis, Any]:
    client = Redis(
        host=test_config.redis.host,
        port=test_config.redis.port,
        password=test_config.redis.password,
        decode_responses=True,
    )
    try:
        await client.ping()
        logger.info(
            "Redis connected successfully on %s:%s",
            test_config.redis.host,
            test_config.redis.port,
        )
    except RedisConnectionError as err:
        logger.error(
            "Redis cannot be connected on %s:%s with error: %s",
            test_config.redis.host,
            test_config.redis.port,
            err,
        )
    yield client
    await client.aclose()


@async_fixture(scope="session")
async def elastic_cli() -> AsyncGenerator[AsyncElasticsearch, Any]:
    client = AsyncElasticsearch(
        hosts=f"http://{test_config.elastic.host}:{test_config.elastic.port}",
        verify_certs=False,
    )
    try:
        await client.ping()
        logger.info(
            "Elasticsearch connected successfully on %s:%s",
            test_config.redis.host,
            test_config.redis.port,
        )
    except ElasticConnectionError as err:
        logger.error(
            "Elasticsearch cannot be connected on %s:%s with error: %s",
            test_config.redis.host,
            test_config.redis.port,
            err,
        )
    yield client
    await client.close()


@fixture(scope="session", autouse=True)
async def create_indexes(elastic_cli: AsyncElasticsearch) -> None:
    results = await gather(
        *[
            create_index(
                elastic_cli,
                name,
                str(
                    Path(__file__).parent
                    / f"testdata/indexes_schemas/{name}.json"
                ),
            )
            for name in test_config.elastic.indexes
        ],
        return_exceptions=True,
    )

    if errors := get_errors(results):
        logger.warning("Indexes created with errors")
        for error in errors:
            logger.error(error)
    else:
        logger.info(
            "Indexes: %s created successfully", test_config.elastic.indexes
        )


@async_fixture(autouse=True)
async def auto_clear_indexes(elastic_cli: AsyncElasticsearch) -> None:
    results = await gather(
        *[
            elastic_cli.delete_by_query(
                index=name,
                body={"query": {"match_all": {}}},
                conflicts="proceed",
            )
            for name in test_config.elastic.indexes
        ],
        return_exceptions=True,
    )

    if errors := get_errors(results):
        logger.warning("Indexes cleared with errors")
        for error in errors:
            logger.error(error)
    else:
        logger.info(
            "Indexes: %s cleared successfully", test_config.elastic.indexes
        )


@async_fixture(autouse=True)
async def auto_clear_cache(redis_cli: Redis) -> None:
    try:
        await redis_cli.flushdb()
        logger.info("Cache was cleared successfully")
    except RedisConnectionError as err:
        logger.error("Redis cannot be connect with error: %s", err)
    except RedisError as err:
        logger.error("Redis cannot clear cache with error: %s", err)
