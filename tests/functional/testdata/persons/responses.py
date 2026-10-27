__all__ = (
    "list_person_films_response",
    "list_person_films_response_filtered",
    "list_person_films_response_filtered_sort_map",
    "list_person_films_response_sort_map",
    "list_person_films_search_response",
    "list_person_films_search_response_sort_map",
    "list_persons_response",
    "list_persons_search_response",
    "list_persons_search_response_sort_map",
    "single_person_response",
)


single_person_response = {
    "uuid": "1a4a8566-61bd-4adb-8f92-bec629ac6b23",
    "full_name": "Butler Good",
    "films": [
        {
            "uuid": "1d650a10-6096-4ed8-b690-b7b8ae370a27",
            "roles": ["actor"],
        },
        {
            "uuid": "35ee2eba-4f1f-4e24-8bc1-a539ed1cfe27",
            "roles": ["writer"],
        },
        {
            "uuid": "3e1a6cc1-0264-4e9c-b310-ae22d0a1881e",
            "roles": ["actor", "writer"],
        },
        {
            "uuid": "a0233d02-ac0e-4275-bc77-fe8a42c8ab9c",
            "roles": ["actor"],
        },
        {
            "uuid": "d5f30330-0a06-4561-aae6-603336c74989",
            "roles": ["director"],
        },
        {
            "uuid": "ee56d3f7-32b5-4739-bd06-79b14a77ded8",
            "roles": ["writer"],
        },
    ],
}

list_persons_response = [
    {
        "uuid": "1a4a8566-61bd-4adb-8f92-bec629ac6b23",
        "full_name": "Butler Good",
        "films": [
            {
                "uuid": "1d650a10-6096-4ed8-b690-b7b8ae370a27",
                "roles": ["actor"],
            },
            {
                "uuid": "35ee2eba-4f1f-4e24-8bc1-a539ed1cfe27",
                "roles": ["writer"],
            },
            {
                "uuid": "3e1a6cc1-0264-4e9c-b310-ae22d0a1881e",
                "roles": ["actor", "writer"],
            },
            {
                "uuid": "a0233d02-ac0e-4275-bc77-fe8a42c8ab9c",
                "roles": ["actor"],
            },
            {
                "uuid": "d5f30330-0a06-4561-aae6-603336c74989",
                "roles": ["director"],
            },
            {
                "uuid": "ee56d3f7-32b5-4739-bd06-79b14a77ded8",
                "roles": ["writer"],
            },
        ],
    },
    {
        "uuid": "27f03701-5756-434a-ba7d-12e663eaa0ac",
        "full_name": "Schmidt Cherry",
        "films": [
            {
                "uuid": "91ff8c5b-211a-4996-80aa-fb8ce324fb42",
                "roles": ["director"],
            },
            {
                "uuid": "a0233d02-ac0e-4275-bc77-fe8a42c8ab9c",
                "roles": ["writer"],
            },
        ],
    },
    {
        "uuid": "401c6b14-c7d4-4c15-9739-fe6b3263c712",
        "full_name": "Marks Weeks",
        "films": [
            {
                "uuid": "28732085-cf64-42fc-91f8-f2d95304c54c",
                "roles": ["actor", "writer", "director"],
            },
            {
                "uuid": "3d695b37-19a7-49d0-9397-860db35beeb6",
                "roles": ["director"],
            },
            {
                "uuid": "91ff8c5b-211a-4996-80aa-fb8ce324fb42",
                "roles": ["writer"],
            },
            {
                "uuid": "f0604021-b297-4a42-ad33-0fe18db48ccf",
                "roles": ["director"],
            },
        ],
    },
    {
        "uuid": "55a4af19-71b7-4d6b-8a50-b625c98bfdfd",
        "full_name": "Kristine Butler",
        "films": [
            {
                "uuid": "1d650a10-6096-4ed8-b690-b7b8ae370a27",
                "roles": ["director"],
            },
            {
                "uuid": "61a6a0df-ed6f-4449-99fa-75ff7c735db3",
                "roles": ["actor", "writer"],
            },
            {
                "uuid": "a548010d-353b-4d3e-bedb-f3d6e5ad3ef6",
                "roles": ["actor"],
            },
            {
                "uuid": "d6bfdb24-cf24-4d87-94d8-c5cadb28c3aa",
                "roles": ["actor"],
            },
            {
                "uuid": "f6b74307-f37c-474a-b7e8-dc9d32cc0df9",
                "roles": ["writer", "director"],
            },
        ],
    },
    {
        "uuid": "583f546e-1ffe-4b67-9fbe-928d705955e8",
        "full_name": "Matthews Pierce",
        "films": [
            {
                "uuid": "1d650a10-6096-4ed8-b690-b7b8ae370a27",
                "roles": ["actor"],
            },
            {
                "uuid": "582c7d16-536f-4a80-81b3-1fbfbeb3d4f1",
                "roles": ["director"],
            },
            {
                "uuid": "62b8fc47-36ac-48e1-8fe6-510a15d1d69b",
                "roles": ["actor"],
            },
            {
                "uuid": "8e20d764-642c-4620-9923-42fc004110ff",
                "roles": ["actor"],
            },
            {
                "uuid": "91ff8c5b-211a-4996-80aa-fb8ce324fb42",
                "roles": ["writer"],
            },
            {
                "uuid": "d5f30330-0a06-4561-aae6-603336c74989",
                "roles": ["actor"],
            },
            {
                "uuid": "e3a8bab1-34ad-4816-b42d-86b03478bd31",
                "roles": ["actor"],
            },
            {
                "uuid": "f0604021-b297-4a42-ad33-0fe18db48ccf",
                "roles": ["director"],
            },
        ],
    },
    {
        "uuid": "5bb94162-1030-4ea1-815d-34cd5cffe143",
        "full_name": "Nichole Pollard",
        "films": [
            {
                "uuid": "28732085-cf64-42fc-91f8-f2d95304c54c",
                "roles": ["director"],
            },
            {
                "uuid": "3d695b37-19a7-49d0-9397-860db35beeb6",
                "roles": ["director"],
            },
            {
                "uuid": "62b8fc47-36ac-48e1-8fe6-510a15d1d69b",
                "roles": ["writer"],
            },
            {
                "uuid": "a0233d02-ac0e-4275-bc77-fe8a42c8ab9c",
                "roles": ["writer"],
            },
            {
                "uuid": "a548010d-353b-4d3e-bedb-f3d6e5ad3ef6",
                "roles": ["director"],
            },
            {
                "uuid": "d6bfdb24-cf24-4d87-94d8-c5cadb28c3aa",
                "roles": ["actor", "writer"],
            },
        ],
    },
    {
        "uuid": "601d0d15-f1d2-415a-a9c7-274e9d7ce27c",
        "full_name": "Owens Hays",
        "films": [
            {
                "uuid": "2f41ee5f-8217-4d9e-8c80-8f8b5038de2a",
                "roles": ["actor"],
            },
            {
                "uuid": "3e1a6cc1-0264-4e9c-b310-ae22d0a1881e",
                "roles": ["writer"],
            },
            {
                "uuid": "42955267-886e-485f-96dc-667575bf8612",
                "roles": ["director"],
            },
            {
                "uuid": "a0233d02-ac0e-4275-bc77-fe8a42c8ab9c",
                "roles": ["director"],
            },
            {
                "uuid": "f0604021-b297-4a42-ad33-0fe18db48ccf",
                "roles": ["director"],
            },
        ],
    },
    {
        "uuid": "6b270cf6-31e0-43d5-8fb3-e998a3e7af9f",
        "full_name": "Christine Velazquez",
        "films": [
            {
                "uuid": "28732085-cf64-42fc-91f8-f2d95304c54c",
                "roles": ["actor"],
            },
            {
                "uuid": "3d695b37-19a7-49d0-9397-860db35beeb6",
                "roles": ["writer"],
            },
            {
                "uuid": "3e1a6cc1-0264-4e9c-b310-ae22d0a1881e",
                "roles": ["director"],
            },
            {
                "uuid": "62b8fc47-36ac-48e1-8fe6-510a15d1d69b",
                "roles": ["director"],
            },
            {
                "uuid": "91ff8c5b-211a-4996-80aa-fb8ce324fb42",
                "roles": ["actor"],
            },
            {
                "uuid": "9b48fb96-f9f8-4ead-b61a-86d46972c3c4",
                "roles": ["actor"],
            },
            {
                "uuid": "f6b74307-f37c-474a-b7e8-dc9d32cc0df9",
                "roles": ["actor"],
            },
        ],
    },
    {
        "uuid": "6e5ce47c-c1d2-408f-9eb1-ed44d76bc25c",
        "full_name": "Klein Davidson",
        "films": [
            {
                "uuid": "1d650a10-6096-4ed8-b690-b7b8ae370a27",
                "roles": ["writer"],
            },
            {
                "uuid": "2f41ee5f-8217-4d9e-8c80-8f8b5038de2a",
                "roles": ["writer"],
            },
            {
                "uuid": "3e1a6cc1-0264-4e9c-b310-ae22d0a1881e",
                "roles": ["director"],
            },
            {
                "uuid": "649b5501-6a88-44db-b7e8-9b453f306329",
                "roles": ["director"],
            },
            {
                "uuid": "8e20d764-642c-4620-9923-42fc004110ff",
                "roles": ["actor"],
            },
            {
                "uuid": "91ff8c5b-211a-4996-80aa-fb8ce324fb42",
                "roles": ["writer", "director"],
            },
            {
                "uuid": "9b48fb96-f9f8-4ead-b61a-86d46972c3c4",
                "roles": ["director"],
            },
            {
                "uuid": "a548010d-353b-4d3e-bedb-f3d6e5ad3ef6",
                "roles": ["actor"],
            },
            {
                "uuid": "e3a8bab1-34ad-4816-b42d-86b03478bd31",
                "roles": ["director"],
            },
            {
                "uuid": "ee56d3f7-32b5-4739-bd06-79b14a77ded8",
                "roles": ["director"],
            },
            {
                "uuid": "f0604021-b297-4a42-ad33-0fe18db48ccf",
                "roles": ["actor"],
            },
        ],
    },
    {
        "uuid": "73100e2e-e612-4c7b-a192-f2f3d6c184e9",
        "full_name": "Parsons Combs",
        "films": [
            {
                "uuid": "2f41ee5f-8217-4d9e-8c80-8f8b5038de2a",
                "roles": ["director"],
            },
            {
                "uuid": "3d695b37-19a7-49d0-9397-860db35beeb6",
                "roles": ["writer"],
            },
            {
                "uuid": "61a6a0df-ed6f-4449-99fa-75ff7c735db3",
                "roles": ["actor"],
            },
            {
                "uuid": "62b8fc47-36ac-48e1-8fe6-510a15d1d69b",
                "roles": ["director"],
            },
            {
                "uuid": "a0233d02-ac0e-4275-bc77-fe8a42c8ab9c",
                "roles": ["director"],
            },
            {
                "uuid": "d5f30330-0a06-4561-aae6-603336c74989",
                "roles": ["director"],
            },
        ],
    },
    {
        "uuid": "78da4d9f-0f30-4358-956c-4a18895c0fb2",
        "full_name": "Byers Schneider",
        "films": [
            {
                "uuid": "0d638f64-b86e-4f0f-939c-c491b0b44f06",
                "roles": ["director"],
            },
            {
                "uuid": "649b5501-6a88-44db-b7e8-9b453f306329",
                "roles": ["actor"],
            },
            {
                "uuid": "78bcec7c-a03b-40f8-b5ff-caf83232d57e",
                "roles": ["writer"],
            },
            {
                "uuid": "91ff8c5b-211a-4996-80aa-fb8ce324fb42",
                "roles": ["director"],
            },
            {
                "uuid": "a548010d-353b-4d3e-bedb-f3d6e5ad3ef6",
                "roles": ["director"],
            },
            {
                "uuid": "ba545b3c-d4f4-4d94-87b9-b1b1f7d8f04d",
                "roles": ["director"],
            },
            {
                "uuid": "d5f30330-0a06-4561-aae6-603336c74989",
                "roles": ["actor"],
            },
            {
                "uuid": "d6bfdb24-cf24-4d87-94d8-c5cadb28c3aa",
                "roles": ["writer"],
            },
        ],
    },
    {
        "uuid": "8b1a5f53-e412-45ac-8d44-a05a433aec4e",
        "full_name": "Green Young",
        "films": [
            {
                "uuid": "582c7d16-536f-4a80-81b3-1fbfbeb3d4f1",
                "roles": ["writer"],
            },
            {
                "uuid": "61a6a0df-ed6f-4449-99fa-75ff7c735db3",
                "roles": ["director"],
            },
            {
                "uuid": "649b5501-6a88-44db-b7e8-9b453f306329",
                "roles": ["director"],
            },
            {
                "uuid": "8e20d764-642c-4620-9923-42fc004110ff",
                "roles": ["director"],
            },
            {
                "uuid": "d5f30330-0a06-4561-aae6-603336c74989",
                "roles": ["writer"],
            },
            {
                "uuid": "f6b74307-f37c-474a-b7e8-dc9d32cc0df9",
                "roles": ["director"],
            },
        ],
    },
    {
        "uuid": "8c2304f3-fac4-44ae-8ed6-7e9ca3854a71",
        "full_name": "Winifred Albert",
        "films": [
            {
                "uuid": "1d650a10-6096-4ed8-b690-b7b8ae370a27",
                "roles": ["writer"],
            },
            {
                "uuid": "42955267-886e-485f-96dc-667575bf8612",
                "roles": ["director"],
            },
            {
                "uuid": "582c7d16-536f-4a80-81b3-1fbfbeb3d4f1",
                "roles": ["writer"],
            },
            {
                "uuid": "649b5501-6a88-44db-b7e8-9b453f306329",
                "roles": ["actor", "director"],
            },
            {
                "uuid": "78bcec7c-a03b-40f8-b5ff-caf83232d57e",
                "roles": ["actor"],
            },
            {
                "uuid": "ee56d3f7-32b5-4739-bd06-79b14a77ded8",
                "roles": ["actor"],
            },
        ],
    },
    {
        "uuid": "959c7366-8594-4f10-8159-db7174149c22",
        "full_name": "Eleanor Gentry",
        "films": [
            {
                "uuid": "0d638f64-b86e-4f0f-939c-c491b0b44f06",
                "roles": ["writer"],
            },
            {
                "uuid": "35ee2eba-4f1f-4e24-8bc1-a539ed1cfe27",
                "roles": ["actor"],
            },
            {
                "uuid": "3d695b37-19a7-49d0-9397-860db35beeb6",
                "roles": ["actor"],
            },
            {
                "uuid": "42955267-886e-485f-96dc-667575bf8612",
                "roles": ["writer"],
            },
            {
                "uuid": "582c7d16-536f-4a80-81b3-1fbfbeb3d4f1",
                "roles": ["actor"],
            },
            {
                "uuid": "61a6a0df-ed6f-4449-99fa-75ff7c735db3",
                "roles": ["actor"],
            },
            {
                "uuid": "a0233d02-ac0e-4275-bc77-fe8a42c8ab9c",
                "roles": ["director"],
            },
            {
                "uuid": "ba545b3c-d4f4-4d94-87b9-b1b1f7d8f04d",
                "roles": ["actor"],
            },
            {
                "uuid": "d6bfdb24-cf24-4d87-94d8-c5cadb28c3aa",
                "roles": ["writer"],
            },
            {
                "uuid": "e3a8bab1-34ad-4816-b42d-86b03478bd31",
                "roles": ["writer"],
            },
        ],
    },
    {
        "uuid": "9875437a-f435-40ca-bc68-90a9969560a0",
        "full_name": "Wilder Ramsey",
        "films": [
            {
                "uuid": "3e1a6cc1-0264-4e9c-b310-ae22d0a1881e",
                "roles": ["director"],
            },
            {
                "uuid": "582c7d16-536f-4a80-81b3-1fbfbeb3d4f1",
                "roles": ["director"],
            },
            {
                "uuid": "62b8fc47-36ac-48e1-8fe6-510a15d1d69b",
                "roles": ["actor", "writer", "director"],
            },
            {
                "uuid": "8e20d764-642c-4620-9923-42fc004110ff",
                "roles": ["writer"],
            },
            {
                "uuid": "f0604021-b297-4a42-ad33-0fe18db48ccf",
                "roles": ["writer"],
            },
        ],
    },
    {
        "uuid": "bb2be48e-b804-4571-b5fc-6426a4105106",
        "full_name": "Goodman Pace",
        "films": [
            {
                "uuid": "0d638f64-b86e-4f0f-939c-c491b0b44f06",
                "roles": ["actor", "writer"],
            },
            {
                "uuid": "1d650a10-6096-4ed8-b690-b7b8ae370a27",
                "roles": ["writer"],
            },
            {
                "uuid": "2f41ee5f-8217-4d9e-8c80-8f8b5038de2a",
                "roles": ["director"],
            },
            {
                "uuid": "3d695b37-19a7-49d0-9397-860db35beeb6",
                "roles": ["actor"],
            },
            {
                "uuid": "62b8fc47-36ac-48e1-8fe6-510a15d1d69b",
                "roles": ["writer"],
            },
            {
                "uuid": "78bcec7c-a03b-40f8-b5ff-caf83232d57e",
                "roles": ["director"],
            },
            {
                "uuid": "a0233d02-ac0e-4275-bc77-fe8a42c8ab9c",
                "roles": ["actor"],
            },
            {
                "uuid": "e3a8bab1-34ad-4816-b42d-86b03478bd31",
                "roles": ["writer", "director"],
            },
            {
                "uuid": "f0604021-b297-4a42-ad33-0fe18db48ccf",
                "roles": ["actor"],
            },
        ],
    },
    {
        "uuid": "e9febf1a-d653-4151-a846-b8d7329a45c7",
        "full_name": "Mclaughlin Neal",
        "films": [
            {
                "uuid": "0d638f64-b86e-4f0f-939c-c491b0b44f06",
                "roles": ["writer"],
            },
            {
                "uuid": "3e1a6cc1-0264-4e9c-b310-ae22d0a1881e",
                "roles": ["actor"],
            },
            {
                "uuid": "42955267-886e-485f-96dc-667575bf8612",
                "roles": ["actor", "director"],
            },
            {
                "uuid": "582c7d16-536f-4a80-81b3-1fbfbeb3d4f1",
                "roles": ["writer"],
            },
            {
                "uuid": "649b5501-6a88-44db-b7e8-9b453f306329",
                "roles": ["writer"],
            },
            {
                "uuid": "d6bfdb24-cf24-4d87-94d8-c5cadb28c3aa",
                "roles": ["director"],
            },
        ],
    },
    {
        "uuid": "ed66851d-8438-44ef-b0af-3de2b6c5f4bc",
        "full_name": "Mallory Salas",
        "films": [
            {
                "uuid": "2f41ee5f-8217-4d9e-8c80-8f8b5038de2a",
                "roles": ["actor"],
            },
            {
                "uuid": "35ee2eba-4f1f-4e24-8bc1-a539ed1cfe27",
                "roles": ["director"],
            },
            {
                "uuid": "649b5501-6a88-44db-b7e8-9b453f306329",
                "roles": ["actor"],
            },
            {
                "uuid": "8e20d764-642c-4620-9923-42fc004110ff",
                "roles": ["actor", "director"],
            },
            {
                "uuid": "ba545b3c-d4f4-4d94-87b9-b1b1f7d8f04d",
                "roles": ["writer"],
            },
            {
                "uuid": "ee56d3f7-32b5-4739-bd06-79b14a77ded8",
                "roles": ["writer", "director"],
            },
            {
                "uuid": "f0604021-b297-4a42-ad33-0fe18db48ccf",
                "roles": ["writer"],
            },
        ],
    },
    {
        "uuid": "f87cc66b-d8d4-4bb1-9d58-59a14c8feda9",
        "full_name": "Kay French",
        "films": [
            {
                "uuid": "28732085-cf64-42fc-91f8-f2d95304c54c",
                "roles": ["writer", "director"],
            },
            {
                "uuid": "35ee2eba-4f1f-4e24-8bc1-a539ed1cfe27",
                "roles": ["writer", "director"],
            },
            {
                "uuid": "9b48fb96-f9f8-4ead-b61a-86d46972c3c4",
                "roles": ["writer"],
            },
            {
                "uuid": "a548010d-353b-4d3e-bedb-f3d6e5ad3ef6",
                "roles": ["writer"],
            },
            {
                "uuid": "ba545b3c-d4f4-4d94-87b9-b1b1f7d8f04d",
                "roles": ["writer"],
            },
            {
                "uuid": "f6b74307-f37c-474a-b7e8-dc9d32cc0df9",
                "roles": ["writer"],
            },
        ],
    },
    {
        "uuid": "fa36d069-50d1-462b-89ba-adaf502cee76",
        "full_name": "Underwood Cunningham",
        "films": [
            {
                "uuid": "0d638f64-b86e-4f0f-939c-c491b0b44f06",
                "roles": ["actor"],
            },
            {
                "uuid": "62b8fc47-36ac-48e1-8fe6-510a15d1d69b",
                "roles": ["actor"],
            },
            {
                "uuid": "a0233d02-ac0e-4275-bc77-fe8a42c8ab9c",
                "roles": ["actor"],
            },
            {
                "uuid": "d5f30330-0a06-4561-aae6-603336c74989",
                "roles": ["writer"],
            },
            {
                "uuid": "ee56d3f7-32b5-4739-bd06-79b14a77ded8",
                "roles": ["writer"],
            },
            {
                "uuid": "f6b74307-f37c-474a-b7e8-dc9d32cc0df9",
                "roles": ["actor"],
            },
        ],
    },
]

list_persons_search_response = [
    {
        "uuid": "1a4a8566-61bd-4adb-8f92-bec629ac6b23",
        "full_name": "Butler Good",
        "films": [
            {
                "uuid": "1d650a10-6096-4ed8-b690-b7b8ae370a27",
                "roles": ["actor"],
            },
            {
                "uuid": "35ee2eba-4f1f-4e24-8bc1-a539ed1cfe27",
                "roles": ["writer"],
            },
            {
                "uuid": "3e1a6cc1-0264-4e9c-b310-ae22d0a1881e",
                "roles": ["actor", "writer"],
            },
            {
                "uuid": "a0233d02-ac0e-4275-bc77-fe8a42c8ab9c",
                "roles": ["actor"],
            },
            {
                "uuid": "d5f30330-0a06-4561-aae6-603336c74989",
                "roles": ["director"],
            },
            {
                "uuid": "ee56d3f7-32b5-4739-bd06-79b14a77ded8",
                "roles": ["writer"],
            },
        ],
    },
    {
        "uuid": "55a4af19-71b7-4d6b-8a50-b625c98bfdfd",
        "full_name": "Kristine Butler",
        "films": [
            {
                "uuid": "1d650a10-6096-4ed8-b690-b7b8ae370a27",
                "roles": ["director"],
            },
            {
                "uuid": "61a6a0df-ed6f-4449-99fa-75ff7c735db3",
                "roles": ["actor", "writer"],
            },
            {
                "uuid": "a548010d-353b-4d3e-bedb-f3d6e5ad3ef6",
                "roles": ["actor"],
            },
            {
                "uuid": "d6bfdb24-cf24-4d87-94d8-c5cadb28c3aa",
                "roles": ["actor"],
            },
            {
                "uuid": "f6b74307-f37c-474a-b7e8-dc9d32cc0df9",
                "roles": ["writer", "director"],
            },
        ],
    },
]

list_persons_search_response_sort_map = {
    "uuid": sorted(
        list_persons_search_response,
        key=lambda item: item["uuid"],
    ),
    "-uuid": sorted(
        list_persons_search_response,
        key=lambda item: item["uuid"],
        reverse=True,
    ),
    "name": sorted(
        list_persons_search_response,
        key=lambda item: item["full_name"],
    ),
    "-name": sorted(
        list_persons_search_response,
        key=lambda item: item["full_name"],
        reverse=True,
    ),
}

list_person_films_response = [
    {
        "uuid": "1d650a10-6096-4ed8-b690-b7b8ae370a27",
        "title": "cupidatat non velit",
        "imdb_rating": 6.5,
    },
    {
        "uuid": "35ee2eba-4f1f-4e24-8bc1-a539ed1cfe27",
        "title": "est consequat sint",
        "imdb_rating": 2.3,
    },
    {
        "uuid": "3e1a6cc1-0264-4e9c-b310-ae22d0a1881e",
        "title": "exercitation consectetur laborum",
        "imdb_rating": 8.9,
    },
    {
        "uuid": "a0233d02-ac0e-4275-bc77-fe8a42c8ab9c",
        "title": "adipisicing esse reprehenderit",
        "imdb_rating": 4.9,
    },
    {
        "uuid": "d5f30330-0a06-4561-aae6-603336c74989",
        "title": "mollit esse ipsum",
        "imdb_rating": 3.4,
    },
    {
        "uuid": "ee56d3f7-32b5-4739-bd06-79b14a77ded8",
        "title": "deserunt dolore officia",
        "imdb_rating": 6.1,
    },
]

list_person_films_response_sort_map = {
    "uuid": sorted(
        list_person_films_response,
        key=lambda item: item["uuid"],
    ),
    "-uuid": sorted(
        list_person_films_response,
        key=lambda item: item["uuid"],
        reverse=True,
    ),
    "imdb_rating": sorted(
        list_person_films_response,
        key=lambda item: item["imdb_rating"],
    ),
    "-imdb_rating": sorted(
        list_person_films_response,
        key=lambda item: item["imdb_rating"],
        reverse=True,
    ),
}

list_person_films_search_response = [
    {
        "uuid": "a0233d02-ac0e-4275-bc77-fe8a42c8ab9c",
        "title": "adipisicing esse reprehenderit",
        "imdb_rating": 4.9,
    },
    {
        "uuid": "d5f30330-0a06-4561-aae6-603336c74989",
        "title": "mollit esse ipsum",
        "imdb_rating": 3.4,
    },
]

list_person_films_search_response_sort_map = {
    "uuid": sorted(
        list_person_films_search_response,
        key=lambda item: item["uuid"],
    ),
    "-uuid": sorted(
        list_person_films_search_response,
        key=lambda item: item["uuid"],
        reverse=True,
    ),
    "imdb_rating": sorted(
        list_person_films_search_response,
        key=lambda item: item["imdb_rating"],
    ),
    "-imdb_rating": sorted(
        list_person_films_search_response,
        key=lambda item: item["imdb_rating"],
        reverse=True,
    ),
}

list_person_films_response_filtered = [
    {
        "uuid": "1d650a10-6096-4ed8-b690-b7b8ae370a27",
        "title": "cupidatat non velit",
        "imdb_rating": 6.5,
    },
    {
        "uuid": "3e1a6cc1-0264-4e9c-b310-ae22d0a1881e",
        "title": "exercitation consectetur laborum",
        "imdb_rating": 8.9,
    },
    {
        "uuid": "ee56d3f7-32b5-4739-bd06-79b14a77ded8",
        "title": "deserunt dolore officia",
        "imdb_rating": 6.1,
    },
]

list_person_films_response_filtered_sort_map = {
    "uuid": sorted(
        list_person_films_response_filtered,
        key=lambda item: item["uuid"],
    ),
    "-uuid": sorted(
        list_person_films_response_filtered,
        key=lambda item: item["uuid"],
        reverse=True,
    ),
    "imdb_rating": sorted(
        list_person_films_response_filtered,
        key=lambda item: item["imdb_rating"],
    ),
    "-imdb_rating": sorted(
        list_person_films_response_filtered,
        key=lambda item: item["imdb_rating"],
        reverse=True,
    ),
}
