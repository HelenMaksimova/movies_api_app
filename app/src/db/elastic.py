from logging import getLogger
from typing import TYPE_CHECKING

from backoff import expo, on_exception
from elasticsearch import (
    AsyncElasticsearch,
    ConnectionError as ElasticConnectionError,
    ConnectionTimeout as ElasticTimeoutError,
)

if TYPE_CHECKING:
    from src.core.config import ElasticConfigDC

__all__ = (
    "elastic",
    "get_client",
    "get_elastic",
)


elastic: AsyncElasticsearch | None = None
logger = getLogger()


@on_exception(expo, (ElasticConnectionError, ElasticTimeoutError), max_tries=5)
async def _ping_client(
    client: AsyncElasticsearch, config: "ElasticConfigDC"
) -> None:
    await client.info()
    logger.info("[Elastic] Was connected on: %s:%s", config.host, config.port)


async def get_client(config: "ElasticConfigDC") -> AsyncElasticsearch | None:
    client = AsyncElasticsearch(
        hosts=[f"http://{config.host}:{config.port}"],
        max_retries=0,
        request_timeout=30,
    )

    try:
        await _ping_client(client, config)
    except Exception as err:
        logger.error("[Elastic] Was not connected with error: %s", err)

    return client


async def get_elastic() -> AsyncElasticsearch | None:
    return elastic
