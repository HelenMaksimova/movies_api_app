from http import HTTPStatus

import pytest
from elasticsearch import AsyncElasticsearch
from settings import test_config
from testdata.genres import (
    list_genres,
    list_genres_response,
    list_genres_response_sort_map,
    single_genre,
    single_genre_response,
)
from utils.base import TestBase
from utils.elastic import write_to_elastic


class BaseTestGenres(TestBase):
    BASE_URL = f"{test_config.app.host}:{test_config.app.port}/api/v1"
    API_URL = "genres/"
    ELASTIC_INDEX = "genres"


class TestGenresItem(BaseTestGenres):
    async def test__get_by_id__success(self, elastic_cli: AsyncElasticsearch):
        await write_to_elastic(elastic_cli, self.ELASTIC_INDEX, [single_genre])

        body, _, status = await self.request(
            url=f"{self.api_url}{single_genre['id']}"
        )

        assert status == HTTPStatus.OK
        assert body == single_genre_response

    async def test__get_by_id__not_found(self):
        body, _, status = await self.request(
            url=f"{self.api_url}{single_genre['id']}"
        )

        assert status == HTTPStatus.NOT_FOUND
        assert body == {"detail": "genre not found"}

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
                        "genre_id",
                    ],
                    "msg": "Input should be a valid UUID, invalid length: expected length 32 "
                    "for simple format, found 3",
                    "type": "uuid_parsing",
                },
            ]
        }


class TestGenresList(BaseTestGenres):
    @pytest.mark.parametrize(
        "params,expected",
        [
            ({}, list_genres_response),
            (
                {"sort": "uuid"},
                list_genres_response_sort_map["uuid"],
            ),
            (
                {"sort": "-uuid"},
                list_genres_response_sort_map["-uuid"],
            ),
            (
                {"sort": "name"},
                list_genres_response_sort_map["name"],
            ),
            (
                {"sort": "-name"},
                list_genres_response_sort_map["-name"],
            ),
            (
                {"sort": "uuid", "page_number": 1, "page_size": 10},
                list_genres_response_sort_map["uuid"],
            ),
            (
                {"sort": "-uuid", "page_number": 1, "page_size": 10},
                list_genres_response_sort_map["-uuid"],
            ),
            (
                {"sort": "name", "page_number": 1, "page_size": 10},
                list_genres_response_sort_map["name"],
            ),
            (
                {"sort": "-name", "page_number": 1, "page_size": 10},
                list_genres_response_sort_map["-name"],
            ),
            (
                {"sort": "uuid", "page_number": 2, "page_size": 20},
                list_genres_response_sort_map["uuid"],
            ),
            (
                {"sort": "-uuid", "page_number": 2, "page_size": 20},
                list_genres_response_sort_map["-uuid"],
            ),
            (
                {"sort": "name", "page_number": 2, "page_size": 20},
                list_genres_response_sort_map["name"],
            ),
            (
                {"sort": "-name", "page_number": 2, "page_size": 20},
                list_genres_response_sort_map["-name"],
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
        await write_to_elastic(elastic_cli, self.ELASTIC_INDEX, list_genres)

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
    async def test__get_list__bad_request(self, params: dict, expected: dict):
        body, _, status = await self.request(**params)

        assert status == HTTPStatus.UNPROCESSABLE_ENTITY
        assert body == {"detail": [expected]}
