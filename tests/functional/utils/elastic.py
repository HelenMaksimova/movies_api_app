from json import JSONDecodeError, loads

from elasticsearch import (
    AsyncElasticsearch,
    ConnectionError,
    Elasticsearch,
    TransportError,
)
from elasticsearch.helpers import async_bulk

__all__ = (
    "create_index",
    "write_to_elastic",
)


async def create_index(
    elastic_cli: Elasticsearch, name: str, schema_file_path: str
) -> None:
    try:
        with open(schema_file_path) as file:
            index_map = loads(file.read())

        if await elastic_cli.indices.exists(index=name):
            await elastic_cli.indices.delete(index=name)
        await elastic_cli.indices.create(index=name, **index_map)

    except IOError as err:
        raise ValueError(
            f"Schema file cannot be opened and read with error: {err}"
        )
    except JSONDecodeError as err:
        raise ValueError(
            f"Schema file cannot be load to json with error: {err}"
        )
    except ConnectionError as err:
        raise ValueError(f"Elasticsearch cannot be connected with error: {err}")
    except TransportError as err:
        raise ValueError(
            f"Elasticsearch cannot create index {name} with error: {err}"
        )


async def write_to_elastic(
    elastic_cli: AsyncElasticsearch, index_name: str, data: list[dict]
) -> None:
    try:
        actions: list[dict] = [
            {
                "_op_type": "update",
                "_index": index_name,
                "_id": row["id"],
                "doc": row,
                "doc_as_upsert": True,
            }
            for row in data
        ]
        updated, errors = await async_bulk(client=elastic_cli, actions=actions)
        await elastic_cli.indices.refresh(index=index_name)

    except ConnectionError as err:
        raise ValueError(f"Elasticsearch cannot be connected with error: {err}")
    except TransportError as err:
        raise ValueError(f"Elasticsearch cannot update data with error: {err}")

    if errors:
        raise ValueError(
            f"Elasticsearch cannot update data. Updated count: {updated}. Errors count: {errors}"
        )
