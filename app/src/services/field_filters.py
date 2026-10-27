from uuid import UUID

__all__ = (
    "genre_filter",
    "person_films_filter",
)


def genre_filter(uuid: UUID) -> dict:
    return {
        "filter": {
            "nested": {"path": "genres", "query": {"term": {"genres.id": uuid}}}
        }
    }


def person_films_filter(uuid: UUID) -> dict:
    return {
        "should": [
            {
                "nested": {
                    "path": "actors",
                    "query": {"term": {"actors.id": uuid}},
                }
            },
            {
                "nested": {
                    "path": "directors",
                    "query": {"term": {"directors.id": uuid}},
                }
            },
            {
                "nested": {
                    "path": "writers",
                    "query": {"term": {"writers.id": uuid}},
                }
            },
        ],
    }
