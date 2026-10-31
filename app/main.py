from contextlib import asynccontextmanager
from logging import config as log_config, getLogger

from fastapi import APIRouter, FastAPI
from fastapi.responses import JSONResponse
from starlette.types import Lifespan
from uvicorn import run

from src.api.v1.film import router as film_router
from src.api.v1.genre import router as genre_router
from src.api.v1.person import router as person_router
from src.core.config import AppConfigDC
from src.core.log_settings import LOGGING
from src.db.elastic import get_client as get_elastic
from src.db.redis import get_client as get_redis

app_config = AppConfigDC()
log_config.dictConfig(LOGGING)


@asynccontextmanager
async def db_lifespan(app: FastAPI):
    app.state.redis = await get_redis(app_config.redis)
    app.state.elastic = await get_elastic(app_config.elastic)
    logger = getLogger()

    try:
        yield

    finally:
        if app.state.redis:
            await app.state.redis.close()
            logger.info("[Redis] Client was closed")

        if app.state.elastic:
            await app.state.elastic.close()
            logger.info("[Elastic] Client was closed")


def set_routers(app: FastAPI):
    v1_router = APIRouter(prefix="/api/v1")

    v1_router.include_router(
        film_router, prefix="/films", tags=["API - версия v1", "Фильмы"]
    )
    v1_router.include_router(
        genre_router, prefix="/genres", tags=["API - версия v1", "Жанры"]
    )
    v1_router.include_router(
        person_router,
        prefix="/persons",
        tags=["API - версия v1", "Участники кинопроизведений"],
    )

    app.include_router(v1_router)


def create_app(
    config: AppConfigDC,
    lifespan: Lifespan | None = None,
    openapi_tags: list[dict] | None = None,
):
    app = FastAPI(
        title=config.project_name,
        description=config.description,
        docs_url="/api/docs",
        openapi_url="/api/openapi.json",
        openapi_tags=openapi_tags,
        default_response_class=JSONResponse,
        lifespan=lifespan,
    )

    set_routers(app)

    return app


app = create_app(
    app_config,
    db_lifespan,
    [
        {
            "name": "API - версия v1",
            "description": "Общий список эндпоинтов API: версия v1",
        },
    ],
)


if __name__ == "__main__":
    run(
        app_config.entrypoint,
        host=app_config.host,
        port=app_config.port,
        log_config=LOGGING,
        log_level=app_config.log_level,
    )
