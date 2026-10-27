from http import HTTPStatus
from typing import Annotated, Any
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Path, Query

from src.services import (
    FilmService,
    PersonService,
    get_film_service,
    get_person_service,
)
from src.api.v1.schemas import (
    DetailPersonResponseSchema,
    ListFilmResponseSchema,
    ListPersonResponseSchema,
    ListSearchFilmQuerySchema,
    ListSearchPersonQuerySchema,
)

__all__ = (
    "person_detail",
    "person_films_list",
    "person_search_list",
    "router",
)


router = APIRouter()


@router.get(
    "/search",
    response_model=ListPersonResponseSchema,
    response_model_by_alias=False,
    summary="Поиск по участникам кинопроизведений",
    description=(
        "Полнотекстовый поиск по именам участников кинопроизведений "
        "с сортировками по имени и идентификатору"
    ),
    response_description=(
        "Список участников кинопроизведений с перечислением "
        "фильмов, в которых они задействованы"
    ),
)
async def person_search_list(
    query: Annotated[ListSearchPersonQuerySchema, Query()],
    person_service: PersonService = Depends(get_person_service),
) -> Any:
    return await person_service.get_list(
        page_number=query.page_number,
        page_size=query.page_size,
        sort=query.sort,
        search_query=query.query,
        is_extended=True,
    )


@router.get(
    "/{person_id}/film",
    response_model=ListFilmResponseSchema,
    response_model_by_alias=False,
    summary="Список фильмов конкретного участника кинопроизведений",
    description=(
        "Список фильмов по идентификатору конкретного участника "
        "кинопроизведений с фильтрацией по жанру и сортировками "
        "по рейтингу и идентификатору фильма"
    ),
    response_description=(
        "Список фильмов конкретного участника кинопроизведений "
        "с указанием рейтинга и названия фильмов"
    ),
)
async def person_films_list(
    query: Annotated[ListSearchFilmQuerySchema, Query()],
    person_id: UUID = Path(description="Идентификатор участника"),
    film_service: FilmService = Depends(get_film_service),
) -> Any:
    return await film_service.get_list(
        page_number=query.page_number,
        page_size=query.page_size,
        sort=query.sort,
        search_query=query.query,
        genre=query.genre,
        person_id=person_id,
    )


@router.get(
    "/{person_id}",
    response_model=DetailPersonResponseSchema,
    response_model_by_alias=False,
    summary="Информация об участнике кинопроизведений",
    description=(
        "Полная информация об участнике кинопроизведений по его идентификатору"
    ),
    response_description=(
        "Информация об участнике кинопроизведений "
        "с указанием списка фильмов в его участием"
    ),
)
async def person_detail(
    person_id: UUID = Path(description="Идентификатор участника"),
    person_service: PersonService = Depends(get_person_service),
) -> Any:
    person = await person_service.get_item(person_id)
    if not person:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="person not found"
        )

    return person
