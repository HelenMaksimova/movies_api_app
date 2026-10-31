from typing import Annotated

from fastapi import Depends

from src.services.film import FilmService, get_film_service
from src.services.genre import GenreService, get_genre_service
from src.services.person import PersonService, get_person_service

__all__ = (
    "DepFilmService",
    "DepGenreService",
    "DepPersonService",
)


DepPersonService = Annotated[PersonService, Depends(get_person_service)]
DepFilmService = Annotated[FilmService, Depends(get_film_service)]
DepGenreService = Annotated[GenreService, Depends(get_genre_service)]
