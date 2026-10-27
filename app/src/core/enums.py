from src.utils.enums import ElasticSortField, SortEnum

__all__ = (
    "FilmSortEnum",
    "GenreSortEnum",
    "PersonSortEnum",
)


class FilmSortEnum(SortEnum):
    imdb_rating = ElasticSortField("imdb_rating")
    imdb_rating_desc = ElasticSortField("-imdb_rating")
    uuid = ElasticSortField("uuid", alias="id")
    uuid_desc = ElasticSortField("-uuid", alias="-id")

    default = uuid


class GenreSortEnum(SortEnum):
    uuid = ElasticSortField("uuid", alias="id")
    uuid_desc = ElasticSortField("-uuid", alias="-id")
    name = ElasticSortField("name", alias="name.raw")
    name_desc = ElasticSortField("-name", alias="-name.raw")

    default = uuid


class PersonSortEnum(SortEnum):
    uuid = ElasticSortField("uuid", alias="id")
    uuid_desc = ElasticSortField("-uuid", alias="-id")
    name = ElasticSortField("name", alias="name.raw")
    name_desc = ElasticSortField("-name", alias="-name.raw")

    default = uuid
