from http import HTTPStatus
from typing import Annotated, Any
from uuid import UUID

from fastapi import APIRouter, HTTPException, Path, Query

from src.api.v1.schemas import (
    DetailFilmResponseSchema,
    ListFilmQuerySchema,
    ListFilmResponseSchema,
    ListSearchFilmQuerySchema,
)
from src.services.dependencies import DepFilmService

__all__ = (
    "film_detail",
    "film_list",
    "film_search_list",
    "router",
)


router = APIRouter()


@router.get(
    "/search",
    response_model=ListFilmResponseSchema,
    response_model_by_alias=False,
    summary="Поиск кинопроизведений",
    description=(
        "Полнотекстовый поиск по названиям кинопроизведений с "
        "фильтрацией по жанру и сортировками по рейтингу и идентификатору"
    ),
    response_description=(
        "Список кинопроизведений с названиями и рейтингами фильмов"
    ),
)
async def film_search_list(
    query: Annotated[ListSearchFilmQuerySchema, Query()],
    film_service: DepFilmService,
) -> Any:
    return await film_service.get_list(
        page_number=query.page_number,
        page_size=query.page_size,
        sort=query.sort,
        search_query=query.query,
        genre=query.genre,
    )


@router.get(
    "/{film_id}",
    response_model=DetailFilmResponseSchema,
    response_model_by_alias=False,
    summary="Информация о кинопроизведении",
    description="Получение информации о кинопроизведении по его идентификатору",
    response_description=(
        "Полная информация о кинопроизведении, "
        "включая список актёров, режиссёров, сценаристов и жанров"
    ),
)
async def film_detail(
    film_id: Annotated[UUID, Path(description="Идентификатор фильма")],
    film_service: DepFilmService,
) -> Any:
    film = await film_service.get_item(film_id)
    if not film:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="film not found"
        )

    return film


@router.get(
    "/",
    response_model=ListFilmResponseSchema,
    response_model_by_alias=False,
    summary="Список кинопроизведений",
    description=(
        "Список кинопроизведений с фильтрацией по жанру "
        "и сортировками по рейтингу и идентификатору"
    ),
    response_description=(
        "Список кинопроизведений с названиями и рейтингами фильмов"
    ),
)
async def film_list(
    query: Annotated[ListFilmQuerySchema, Query()],
    film_service: DepFilmService,
) -> Any:
    return await film_service.get_list(
        page_number=query.page_number,
        page_size=query.page_size,
        sort=query.sort,
        genre=query.genre,
    )
