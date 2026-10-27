from http import HTTPStatus

import pytest
from elasticsearch import AsyncElasticsearch
from settings import test_config
from testdata.films import (
    list_films,
    list_films_response,
    list_films_response_filtered,
    list_films_response_filtered_sort_map,
    list_films_response_sort_map,
    list_films_search_response,
    list_films_search_response_filtered,
    list_films_search_response_filtered_sort_map,
    list_films_search_response_sort_map,
    single_film,
    single_film_response,
)
from utils.base import TestBase
from utils.elastic import write_to_elastic


class BaseTestFilms(TestBase):
    BASE_URL = f"{test_config.app.host}:{test_config.app.port}/api/v1"
    API_URL = "films/"
    ELASTIC_INDEX = "movies"


class TestFilmsItem(BaseTestFilms):
    async def test__get_by_id__success(self, elastic_cli: AsyncElasticsearch):
        await write_to_elastic(elastic_cli, self.ELASTIC_INDEX, [single_film])

        body, _, status = await self.request(
            url=f"{self.api_url}{single_film['id']}"
        )

        assert status == HTTPStatus.OK
        assert body == single_film_response

    async def test__get_by_id__not_found(self):
        body, _, status = await self.request(
            url=f"{self.api_url}{single_film['id']}"
        )

        assert status == HTTPStatus.NOT_FOUND
        assert body == {"detail": "film not found"}

    async def test__get_by_id__bad_request(self):
        body, _, status = await self.request(url=f"{self.api_url}{'abc'}")

        assert status == HTTPStatus.UNPROCESSABLE_ENTITY
        assert body == {
            "detail": [
                {
                    "ctx": {
                        "error": "invalid length: expected length 32 for simple format, found 3",
                    },
                    "input": "abc",
                    "loc": [
                        "path",
                        "film_id",
                    ],
                    "msg": "Input should be a valid UUID, invalid length: expected length 32 "
                    "for simple format, found 3",
                    "type": "uuid_parsing",
                },
            ]
        }


class TestFilmsList(BaseTestFilms):
    @pytest.mark.parametrize(
        "params,expected",
        [
            ({}, list_films_response),
            (
                {"sort": "uuid"},
                list_films_response_sort_map["uuid"],
            ),
            (
                {"sort": "-uuid"},
                list_films_response_sort_map["-uuid"],
            ),
            (
                {"sort": "imdb_rating"},
                list_films_response_sort_map["imdb_rating"],
            ),
            (
                {"sort": "-imdb_rating"},
                list_films_response_sort_map["-imdb_rating"],
            ),
            (
                {"sort": "uuid", "page_number": 1, "page_size": 10},
                list_films_response_sort_map["uuid"],
            ),
            (
                {"sort": "-uuid", "page_number": 1, "page_size": 10},
                list_films_response_sort_map["-uuid"],
            ),
            (
                {"sort": "imdb_rating", "page_number": 1, "page_size": 10},
                list_films_response_sort_map["imdb_rating"],
            ),
            (
                {"sort": "-imdb_rating", "page_number": 1, "page_size": 10},
                list_films_response_sort_map["-imdb_rating"],
            ),
            (
                {"sort": "uuid", "page_number": 2, "page_size": 20},
                list_films_response_sort_map["uuid"],
            ),
            (
                {"sort": "-uuid", "page_number": 2, "page_size": 20},
                list_films_response_sort_map["-uuid"],
            ),
            (
                {"sort": "imdb_rating", "page_number": 2, "page_size": 20},
                list_films_response_sort_map["imdb_rating"],
            ),
            (
                {"sort": "-imdb_rating", "page_number": 2, "page_size": 20},
                list_films_response_sort_map["-imdb_rating"],
            ),
            (
                {"genre": "430fdde0-b194-4167-a915-c23c53384ba3"},
                list_films_response_filtered,
            ),
            (
                {"genre": "630fdde0-b184-4167-a915-c23c53384ba1"},
                [],
            ),
            (
                {
                    "genre": "430fdde0-b194-4167-a915-c23c53384ba3",
                    "sort": "uuid",
                },
                list_films_response_filtered_sort_map["uuid"],
            ),
            (
                {
                    "genre": "430fdde0-b194-4167-a915-c23c53384ba3",
                    "sort": "-uuid",
                },
                list_films_response_filtered_sort_map["-uuid"],
            ),
            (
                {
                    "genre": "430fdde0-b194-4167-a915-c23c53384ba3",
                    "sort": "imdb_rating",
                },
                list_films_response_filtered_sort_map["imdb_rating"],
            ),
            (
                {
                    "genre": "430fdde0-b194-4167-a915-c23c53384ba3",
                    "sort": "-imdb_rating",
                },
                list_films_response_filtered_sort_map["-imdb_rating"],
            ),
            (
                {
                    "genre": "430fdde0-b194-4167-a915-c23c53384ba3",
                    "sort": "uuid",
                    "page_number": 1,
                    "page_size": 10,
                },
                list_films_response_filtered_sort_map["uuid"],
            ),
            (
                {
                    "genre": "430fdde0-b194-4167-a915-c23c53384ba3",
                    "sort": "-uuid",
                    "page_number": 1,
                    "page_size": 10,
                },
                list_films_response_filtered_sort_map["-uuid"],
            ),
            (
                {
                    "genre": "430fdde0-b194-4167-a915-c23c53384ba3",
                    "sort": "imdb_rating",
                    "page_number": 1,
                    "page_size": 10,
                },
                list_films_response_filtered_sort_map["imdb_rating"],
            ),
            (
                {
                    "genre": "430fdde0-b194-4167-a915-c23c53384ba3",
                    "sort": "-imdb_rating",
                    "page_number": 1,
                    "page_size": 10,
                },
                list_films_response_filtered_sort_map["-imdb_rating"],
            ),
            (
                {
                    "genre": "430fdde0-b194-4167-a915-c23c53384ba3",
                    "sort": "uuid",
                    "page_number": 2,
                    "page_size": 3,
                },
                list_films_response_filtered_sort_map["uuid"],
            ),
            (
                {
                    "genre": "430fdde0-b194-4167-a915-c23c53384ba3",
                    "sort": "-uuid",
                    "page_number": 2,
                    "page_size": 3,
                },
                list_films_response_filtered_sort_map["-uuid"],
            ),
            (
                {
                    "genre": "430fdde0-b194-4167-a915-c23c53384ba3",
                    "sort": "imdb_rating",
                    "page_number": 2,
                    "page_size": 3,
                },
                list_films_response_filtered_sort_map["imdb_rating"],
            ),
            (
                {
                    "genre": "430fdde0-b194-4167-a915-c23c53384ba3",
                    "sort": "-imdb_rating",
                    "page_number": 2,
                    "page_size": 3,
                },
                list_films_response_filtered_sort_map["-imdb_rating"],
            ),
        ],
    )
    async def test__get_list__success(
        self,
        elastic_cli: AsyncElasticsearch,
        params: dict,
        expected: list[dict],
    ):
        page = params.get("page_number", 1)
        size = params.get("page_size", 50)
        await write_to_elastic(elastic_cli, self.ELASTIC_INDEX, list_films)

        body, _, status = await self.request(**params)

        assert status == HTTPStatus.OK
        assert body == expected[size * (page - 1) : page * size]

    @pytest.mark.parametrize(
        "params,expected",
        [
            (
                {"page_number": 0},
                {
                    "ctx": {"gt": 0},
                    "input": "0",
                    "loc": ["query", "page_number"],
                    "msg": "Input should be greater than 0",
                    "type": "greater_than",
                },
            ),
            (
                {"page_size": 0},
                {
                    "ctx": {"gt": 0},
                    "input": "0",
                    "loc": ["query", "page_size"],
                    "msg": "Input should be greater than 0",
                    "type": "greater_than",
                },
            ),
            (
                {"page_size": 101},
                {
                    "ctx": {"le": 100},
                    "input": "101",
                    "loc": ["query", "page_size"],
                    "msg": "Input should be less than or equal to 100",
                    "type": "less_than_equal",
                },
            ),
            (
                {"page_number": "abc"},
                {
                    "input": "abc",
                    "loc": ["query", "page_number"],
                    "msg": "Input should be a valid integer, unable to parse string "
                    "as an integer",
                    "type": "int_parsing",
                },
            ),
            (
                {"page_size": "abc"},
                {
                    "input": "abc",
                    "loc": ["query", "page_size"],
                    "msg": "Input should be a valid integer, unable to parse string "
                    "as an integer",
                    "type": "int_parsing",
                },
            ),
            (
                {"page_number": ""},
                {
                    "input": "",
                    "loc": ["query", "page_number"],
                    "msg": "Input should be a valid integer, unable to parse string "
                    "as an integer",
                    "type": "int_parsing",
                },
            ),
            (
                {"page_size": ""},
                {
                    "input": "",
                    "loc": ["query", "page_size"],
                    "msg": "Input should be a valid integer, unable to parse string "
                    "as an integer",
                    "type": "int_parsing",
                },
            ),
            (
                {"sort": "some"},
                {
                    "ctx": {"error": {}},
                    "input": "some",
                    "loc": ["query", "sort"],
                    "msg": "Value error, Sort must be one of: ['-imdb_rating', '-uuid', 'imdb_rating', 'uuid']",
                    "type": "value_error",
                },
            ),
            (
                {"genre": "some"},
                {
                    "ctx": {
                        "error": "invalid character: expected an optional prefix of `urn:uuid:` "
                        "followed by [0-9a-fA-F-], found `s` at 1",
                    },
                    "input": "some",
                    "loc": [
                        "query",
                        "genre",
                    ],
                    "msg": "Input should be a valid UUID, invalid character: expected an "
                    "optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found "
                    "`s` at 1",
                    "type": "uuid_parsing",
                },
            ),
        ],
    )
    async def test__get_list__bad_request(self, params: dict, expected: dict):
        body, _, status = await self.request(**params)

        assert status == HTTPStatus.UNPROCESSABLE_ENTITY
        assert body == {"detail": [expected]}


class TestFilmSearch(BaseTestFilms):
    API_URL = "films/search"

    @pytest.mark.parametrize(
        "params,expected",
        [
            ({}, list_films_response),
            (
                {"query": "esse"},
                list_films_search_response,
            ),
            (
                {"sort": "uuid", "query": "esse"},
                list_films_search_response_sort_map["uuid"],
            ),
            (
                {"sort": "-uuid", "query": "esse"},
                list_films_search_response_sort_map["-uuid"],
            ),
            (
                {"sort": "imdb_rating", "query": "esse"},
                list_films_search_response_sort_map["imdb_rating"],
            ),
            (
                {"sort": "-imdb_rating", "query": "esse"},
                list_films_search_response_sort_map["-imdb_rating"],
            ),
            (
                {
                    "sort": "uuid",
                    "page_number": 1,
                    "page_size": 10,
                    "query": "esse",
                },
                list_films_search_response_sort_map["uuid"],
            ),
            (
                {
                    "sort": "-uuid",
                    "page_number": 1,
                    "page_size": 10,
                    "query": "esse",
                },
                list_films_search_response_sort_map["-uuid"],
            ),
            (
                {
                    "sort": "imdb_rating",
                    "page_number": 1,
                    "page_size": 10,
                    "query": "esse",
                },
                list_films_search_response_sort_map["imdb_rating"],
            ),
            (
                {
                    "sort": "-imdb_rating",
                    "page_number": 1,
                    "page_size": 10,
                    "query": "esse",
                },
                list_films_search_response_sort_map["-imdb_rating"],
            ),
            (
                {
                    "sort": "uuid",
                    "page_number": 2,
                    "page_size": 20,
                    "query": "esse",
                },
                list_films_search_response_sort_map["uuid"],
            ),
            (
                {
                    "sort": "-uuid",
                    "page_number": 2,
                    "page_size": 20,
                    "query": "esse",
                },
                list_films_search_response_sort_map["-uuid"],
            ),
            (
                {
                    "sort": "imdb_rating",
                    "page_number": 2,
                    "page_size": 20,
                    "query": "esse",
                },
                list_films_search_response_sort_map["imdb_rating"],
            ),
            (
                {
                    "sort": "-imdb_rating",
                    "page_number": 2,
                    "page_size": 20,
                    "query": "esse",
                },
                list_films_search_response_sort_map["-imdb_rating"],
            ),
            (
                {
                    "genre": "430fdde0-b194-4167-a915-c23c53384ba3",
                    "query": "esse",
                },
                list_films_search_response_filtered,
            ),
            (
                {
                    "genre": "630fdde0-b184-4167-a915-c23c53384ba1",
                    "query": "esse",
                },
                [],
            ),
            (
                {"query": "somesome"},
                [],
            ),
            (
                {"query": ""},
                list_films_response,
            ),
            (
                {
                    "genre": "430fdde0-b194-4167-a915-c23c53384ba3",
                    "sort": "uuid",
                    "query": "esse",
                },
                list_films_search_response_filtered_sort_map["uuid"],
            ),
            (
                {
                    "genre": "430fdde0-b194-4167-a915-c23c53384ba3",
                    "sort": "-uuid",
                    "query": "esse",
                },
                list_films_search_response_filtered_sort_map["-uuid"],
            ),
            (
                {
                    "genre": "430fdde0-b194-4167-a915-c23c53384ba3",
                    "sort": "imdb_rating",
                    "query": "esse",
                },
                list_films_search_response_filtered_sort_map["imdb_rating"],
            ),
            (
                {
                    "genre": "430fdde0-b194-4167-a915-c23c53384ba3",
                    "sort": "-imdb_rating",
                    "query": "esse",
                },
                list_films_search_response_filtered_sort_map["-imdb_rating"],
            ),
            (
                {
                    "genre": "430fdde0-b194-4167-a915-c23c53384ba3",
                    "sort": "uuid",
                    "page_number": 1,
                    "page_size": 10,
                    "query": "esse",
                },
                list_films_search_response_filtered_sort_map["uuid"],
            ),
            (
                {
                    "genre": "430fdde0-b194-4167-a915-c23c53384ba3",
                    "sort": "-uuid",
                    "page_number": 1,
                    "page_size": 10,
                    "query": "esse",
                },
                list_films_search_response_filtered_sort_map["-uuid"],
            ),
            (
                {
                    "genre": "430fdde0-b194-4167-a915-c23c53384ba3",
                    "sort": "imdb_rating",
                    "page_number": 1,
                    "page_size": 10,
                    "query": "esse",
                },
                list_films_search_response_filtered_sort_map["imdb_rating"],
            ),
            (
                {
                    "genre": "430fdde0-b194-4167-a915-c23c53384ba3",
                    "sort": "-imdb_rating",
                    "page_number": 1,
                    "page_size": 10,
                    "query": "esse",
                },
                list_films_search_response_filtered_sort_map["-imdb_rating"],
            ),
            (
                {
                    "genre": "430fdde0-b194-4167-a915-c23c53384ba3",
                    "sort": "uuid",
                    "page_number": 2,
                    "page_size": 3,
                    "query": "esse",
                },
                list_films_search_response_filtered_sort_map["uuid"],
            ),
            (
                {
                    "genre": "430fdde0-b194-4167-a915-c23c53384ba3",
                    "sort": "-uuid",
                    "page_number": 2,
                    "page_size": 3,
                    "query": "esse",
                },
                list_films_search_response_filtered_sort_map["-uuid"],
            ),
            (
                {
                    "genre": "430fdde0-b194-4167-a915-c23c53384ba3",
                    "sort": "imdb_rating",
                    "page_number": 2,
                    "page_size": 3,
                    "query": "esse",
                },
                list_films_search_response_filtered_sort_map["imdb_rating"],
            ),
            (
                {
                    "genre": "430fdde0-b194-4167-a915-c23c53384ba3",
                    "sort": "-imdb_rating",
                    "page_number": 2,
                    "page_size": 3,
                    "query": "esse",
                },
                list_films_search_response_filtered_sort_map["-imdb_rating"],
            ),
        ],
    )
    async def test__search_list__success(
        self,
        elastic_cli: AsyncElasticsearch,
        params: dict,
        expected: list[dict],
    ):
        page = params.get("page_number", 1)
        size = params.get("page_size", 50)
        await write_to_elastic(elastic_cli, self.ELASTIC_INDEX, list_films)

        body, _, status = await self.request(**params)

        assert status == HTTPStatus.OK
        assert body == expected[size * (page - 1) : page * size]

    @pytest.mark.parametrize(
        "params,expected",
        [
            (
                {"page_number": 0},
                {
                    "ctx": {"gt": 0},
                    "input": "0",
                    "loc": ["query", "page_number"],
                    "msg": "Input should be greater than 0",
                    "type": "greater_than",
                },
            ),
            (
                {"page_size": 0},
                {
                    "ctx": {"gt": 0},
                    "input": "0",
                    "loc": ["query", "page_size"],
                    "msg": "Input should be greater than 0",
                    "type": "greater_than",
                },
            ),
            (
                {"page_size": 101},
                {
                    "ctx": {"le": 100},
                    "input": "101",
                    "loc": ["query", "page_size"],
                    "msg": "Input should be less than or equal to 100",
                    "type": "less_than_equal",
                },
            ),
            (
                {"page_number": "abc"},
                {
                    "input": "abc",
                    "loc": ["query", "page_number"],
                    "msg": "Input should be a valid integer, unable to parse string "
                    "as an integer",
                    "type": "int_parsing",
                },
            ),
            (
                {"page_size": "abc"},
                {
                    "input": "abc",
                    "loc": ["query", "page_size"],
                    "msg": "Input should be a valid integer, unable to parse string "
                    "as an integer",
                    "type": "int_parsing",
                },
            ),
            (
                {"page_number": ""},
                {
                    "input": "",
                    "loc": ["query", "page_number"],
                    "msg": "Input should be a valid integer, unable to parse string "
                    "as an integer",
                    "type": "int_parsing",
                },
            ),
            (
                {"page_size": ""},
                {
                    "input": "",
                    "loc": ["query", "page_size"],
                    "msg": "Input should be a valid integer, unable to parse string "
                    "as an integer",
                    "type": "int_parsing",
                },
            ),
            (
                {"sort": "some"},
                {
                    "ctx": {"error": {}},
                    "input": "some",
                    "loc": ["query", "sort"],
                    "msg": "Value error, Sort must be one of: ['-imdb_rating', '-uuid', 'imdb_rating', 'uuid']",
                    "type": "value_error",
                },
            ),
            (
                {"genre": "some"},
                {
                    "ctx": {
                        "error": "invalid character: expected an optional prefix of `urn:uuid:` "
                        "followed by [0-9a-fA-F-], found `s` at 1",
                    },
                    "input": "some",
                    "loc": [
                        "query",
                        "genre",
                    ],
                    "msg": "Input should be a valid UUID, invalid character: expected an "
                    "optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found "
                    "`s` at 1",
                    "type": "uuid_parsing",
                },
            ),
        ],
    )
    async def test__search_list__bad_request(
        self, params: dict, expected: dict
    ):
        body, _, status = await self.request(**params)

        assert status == HTTPStatus.UNPROCESSABLE_ENTITY
        assert body == {"detail": [expected]}
