from http import HTTPStatus

import pytest
from elasticsearch import AsyncElasticsearch
from settings import test_config
from testdata.films import list_films
from testdata.persons import (
    list_person_films_response,
    list_person_films_response_filtered,
    list_person_films_response_filtered_sort_map,
    list_person_films_response_sort_map,
    list_person_films_search_response,
    list_person_films_search_response_sort_map,
    list_persons,
    list_persons_response,
    list_persons_search_response,
    list_persons_search_response_sort_map,
    single_person,
    single_person_response,
)
from utils.base import TestBase
from utils.elastic import write_to_elastic


class BaseTestPersons(TestBase):
    BASE_URL = f"{test_config.app.host}:{test_config.app.port}/api/v1"
    API_URL = "persons/"
    ELASTIC_INDEX = "persons"


class TestPersonItem(BaseTestPersons):
    async def test__get_by_id__success(self, elastic_cli: AsyncElasticsearch):
        await write_to_elastic(elastic_cli, self.ELASTIC_INDEX, [single_person])

        body, _, status = await self.request(
            url=f"{self.api_url}{single_person['id']}"
        )

        assert status == HTTPStatus.OK
        assert body == single_person_response

    async def test__get_by_id__not_found(self):
        body, _, status = await self.request(
            url=f"{self.api_url}{single_person['id']}"
        )

        assert status == HTTPStatus.NOT_FOUND
        assert body == {"detail": "person not found"}

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
                        "person_id",
                    ],
                    "msg": "Input should be a valid UUID, invalid length: expected length 32 "
                    "for simple format, found 3",
                    "type": "uuid_parsing",
                },
            ]
        }


class TestPersonSearch(BaseTestPersons):
    API_URL = "persons/search"

    @pytest.mark.parametrize(
        "params,expected",
        [
            ({}, list_persons_response),
            (
                {"query": "butler"},
                list_persons_search_response,
            ),
            (
                {"sort": "uuid", "query": "butler"},
                list_persons_search_response_sort_map["uuid"],
            ),
            (
                {"sort": "-uuid", "query": "butler"},
                list_persons_search_response_sort_map["-uuid"],
            ),
            (
                {"sort": "name", "query": "butler"},
                list_persons_search_response_sort_map["name"],
            ),
            (
                {"sort": "-name", "query": "butler"},
                list_persons_search_response_sort_map["-name"],
            ),
            (
                {
                    "sort": "uuid",
                    "page_number": 1,
                    "page_size": 10,
                    "query": "butler",
                },
                list_persons_search_response_sort_map["uuid"],
            ),
            (
                {
                    "sort": "-uuid",
                    "page_number": 1,
                    "page_size": 10,
                    "query": "butler",
                },
                list_persons_search_response_sort_map["-uuid"],
            ),
            (
                {
                    "sort": "name",
                    "page_number": 1,
                    "page_size": 10,
                    "query": "butler",
                },
                list_persons_search_response_sort_map["name"],
            ),
            (
                {
                    "sort": "-name",
                    "page_number": 1,
                    "page_size": 10,
                    "query": "butler",
                },
                list_persons_search_response_sort_map["-name"],
            ),
            (
                {
                    "sort": "uuid",
                    "page_number": 2,
                    "page_size": 1,
                    "query": "butler",
                },
                list_persons_search_response_sort_map["uuid"],
            ),
            (
                {
                    "sort": "-uuid",
                    "page_number": 2,
                    "page_size": 1,
                    "query": "butler",
                },
                list_persons_search_response_sort_map["-uuid"],
            ),
            (
                {
                    "sort": "name",
                    "page_number": 2,
                    "page_size": 1,
                    "query": "butler",
                },
                list_persons_search_response_sort_map["name"],
            ),
            (
                {
                    "sort": "-name",
                    "page_number": 2,
                    "page_size": 1,
                    "query": "butler",
                },
                list_persons_search_response_sort_map["-name"],
            ),
            (
                {"query": "somesome"},
                [],
            ),
            (
                {"query": ""},
                list_persons_response,
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
        await write_to_elastic(elastic_cli, self.ELASTIC_INDEX, list_persons)

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
                    "msg": "Value error, Sort must be one of: ['-name', '-uuid', 'name', 'uuid']",
                    "type": "value_error",
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


class TestPersonFilmsList(BaseTestPersons):
    @pytest.mark.parametrize(
        "params,expected",
        [
            ({}, list_person_films_response),
            (
                {"sort": "uuid"},
                list_person_films_response_sort_map["uuid"],
            ),
            (
                {"sort": "-uuid"},
                list_person_films_response_sort_map["-uuid"],
            ),
            (
                {"sort": "imdb_rating"},
                list_person_films_response_sort_map["imdb_rating"],
            ),
            (
                {"sort": "-imdb_rating"},
                list_person_films_response_sort_map["-imdb_rating"],
            ),
            (
                {
                    "sort": "uuid",
                    "page_number": 1,
                    "page_size": 10,
                },
                list_person_films_response_sort_map["uuid"],
            ),
            (
                {
                    "sort": "-uuid",
                    "page_number": 1,
                    "page_size": 10,
                },
                list_person_films_response_sort_map["-uuid"],
            ),
            (
                {
                    "sort": "imdb_rating",
                    "page_number": 1,
                    "page_size": 10,
                },
                list_person_films_response_sort_map["imdb_rating"],
            ),
            (
                {
                    "sort": "-imdb_rating",
                    "page_number": 1,
                    "page_size": 10,
                },
                list_person_films_response_sort_map["-imdb_rating"],
            ),
            (
                {
                    "sort": "uuid",
                    "page_number": 2,
                    "page_size": 3,
                },
                list_person_films_response_sort_map["uuid"],
            ),
            (
                {
                    "sort": "-uuid",
                    "page_number": 2,
                    "page_size": 3,
                },
                list_person_films_response_sort_map["-uuid"],
            ),
            (
                {
                    "sort": "imdb_rating",
                    "page_number": 2,
                    "page_size": 3,
                },
                list_person_films_response_sort_map["imdb_rating"],
            ),
            (
                {
                    "sort": "-imdb_rating",
                    "page_number": 2,
                    "page_size": 3,
                },
                list_person_films_response_sort_map["-imdb_rating"],
            ),
            (
                {"query": "esse"},
                list_person_films_search_response,
            ),
            (
                {"query": "somesome"},
                [],
            ),
            (
                {"query": ""},
                list_person_films_response,
            ),
            (
                {"query": "esse", "sort": "uuid"},
                list_person_films_search_response_sort_map["uuid"],
            ),
            (
                {"query": "esse", "sort": "-uuid"},
                list_person_films_search_response_sort_map["-uuid"],
            ),
            (
                {"query": "esse", "sort": "imdb_rating"},
                list_person_films_search_response_sort_map["imdb_rating"],
            ),
            (
                {"query": "esse", "sort": "-imdb_rating"},
                list_person_films_search_response_sort_map["-imdb_rating"],
            ),
            (
                {"genre": "da7bdf5c-8b83-42bb-b0c6-5f75f253be3e"},
                list_person_films_response_filtered,
            ),
            (
                {
                    "genre": "da7bdf5c-8b83-42bb-b0c6-5f75f253be3e",
                    "sort": "uuid",
                },
                list_person_films_response_filtered_sort_map["uuid"],
            ),
            (
                {
                    "genre": "da7bdf5c-8b83-42bb-b0c6-5f75f253be3e",
                    "sort": "-uuid",
                },
                list_person_films_response_filtered_sort_map["-uuid"],
            ),
            (
                {
                    "genre": "da7bdf5c-8b83-42bb-b0c6-5f75f253be3e",
                    "sort": "imdb_rating",
                },
                list_person_films_response_filtered_sort_map["imdb_rating"],
            ),
            (
                {
                    "genre": "da7bdf5c-8b83-42bb-b0c6-5f75f253be3e",
                    "sort": "-imdb_rating",
                },
                list_person_films_response_filtered_sort_map["-imdb_rating"],
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
        url = f"{self.api_url}{single_person['id']}/film/"
        await write_to_elastic(elastic_cli, "movies", list_films)

        body, _, status = await self.request(url, **params)

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
        url = f"{self.api_url}{single_person['id']}/film/"

        body, _, status = await self.request(url, **params)

        assert status == HTTPStatus.UNPROCESSABLE_ENTITY
        assert body == {"detail": [expected]}

    async def test__get_list__bad_person_id_request(self):
        url = f"{self.api_url}{'abc'}/film/"

        body, _, status = await self.request(url)

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
                        "person_id",
                    ],
                    "msg": "Input should be a valid UUID, invalid length: expected length 32 "
                    "for simple format, found 3",
                    "type": "uuid_parsing",
                }
            ]
        }
