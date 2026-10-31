from http import HTTPStatus
from typing import Annotated, Any
from uuid import UUID

from fastapi import APIRouter, HTTPException, Path, Query

from src.api.v1.schemas import (
    DetailGenreResponseSchema,
    ListGenreQuerySchema,
    ListGenreResponseSchema,
)
from src.services.dependencies import DepGenreService

__all__ = (
    "genre_detail",
    "genre_list",
    "router",
)


router = APIRouter()


@router.get(
    "/{genre_id}",
    response_model=DetailGenreResponseSchema,
    response_model_by_alias=False,
    summary="Информация о жанре",
    description="Получение информации о жанре по идентификатору",
    response_description="Название и описание жанра",
)
async def genre_detail(
    genre_id: Annotated[UUID, Path(description="Идентификатор жанра")],
    genre_service: DepGenreService,
) -> Any:
    genre = await genre_service.get_item(genre_id)
    if not genre:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="genre not found"
        )

    return genre


@router.get(
    "/",
    response_model=ListGenreResponseSchema,
    response_model_by_alias=False,
    summary="Список жанров",
    description="Список жанров с сортировками по идентификатору и названию",
    response_description="Название и описание жанра",
)
async def genre_list(
    query: Annotated[ListGenreQuerySchema, Query()],
    genre_service: DepGenreService,
) -> Any:
    return await genre_service.get_list(
        page_number=query.page_number,
        page_size=query.page_size,
        sort=query.sort,
        is_extended=True,
    )
