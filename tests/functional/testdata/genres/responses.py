__all__ = (
    "list_genres_response",
    "list_genres_response_sort_map",
    "single_genre_response",
)


single_genre_response = {
    "uuid": "5bef14c8-37de-4842-b492-29c36ebb8a56",
    "name": "Single",
    "description": "Some description",
}

list_genres_response = [
    {
        "uuid": "00928a9c-77ef-4dcc-9254-b07eadba1f14",
        "name": "C-Genre",
        "description": "Some description C",
    },
    {
        "uuid": "0fd193a7-8679-40f3-acf1-64b715d797d3",
        "name": "D-Genre",
        "description": "Some description D",
    },
    {
        "uuid": "1870dbec-6e3d-4505-86d8-c04ce02793ca",
        "name": "A-Genre",
        "description": "Some description A",
    },
    {
        "uuid": "1acc2a8d-b1ac-4857-a27d-8f6b9fd046ac",
        "name": "H-Genre",
        "description": "Some description H",
    },
    {
        "uuid": "1d388712-423f-4601-a87b-d49355a101c9",
        "name": "N-Genre",
        "description": "Some description N",
    },
    {
        "uuid": "1e5818ba-db0c-4e1d-8878-fdbac5fabcc0",
        "name": "V-Genre",
        "description": "Some description V",
    },
    {
        "uuid": "22912fba-d086-4e39-80a4-7ca20dc8d48d",
        "name": "E-Genre",
        "description": "Some description E",
    },
    {
        "uuid": "266eb9bc-e0e7-497f-a394-c21562da57fa",
        "name": "T-Genre",
        "description": "Some description T",
    },
    {
        "uuid": "2833d0db-59ed-4ba6-9ff9-7b7cfa1e3530",
        "name": "R-Genre",
        "description": "Some description R",
    },
    {
        "uuid": "2e7ad6f5-a5b4-4e37-b927-4c693412262e",
        "name": "F-Genre",
        "description": "Some description F",
    },
    {
        "uuid": "328ae035-b4e4-4072-ac6f-3451eba2fedc",
        "name": "I-Genre",
        "description": "Some description I",
    },
    {
        "uuid": "430fdde0-b194-4167-a915-c23c53384ba3",
        "name": "L-Genre",
        "description": "Some description L",
    },
    {
        "uuid": "574d1617-5d1c-4e6f-b44e-e070142ebb0f",
        "name": "X-Genre",
        "description": "Some description X",
    },
    {
        "uuid": "5ff663a3-a164-4947-9801-1cf3e8a9db7b",
        "name": "B-Genre",
        "description": "Some description B",
    },
    {
        "uuid": "60d74606-9b87-44de-8884-1b830688c94e",
        "name": "W-Genre",
        "description": "Some description W",
    },
    {
        "uuid": "61c8b1b5-8232-4239-84c6-b8cdabc5c1e6",
        "name": "S-Genre",
        "description": None,
    },
    {
        "uuid": "71a794bc-14e9-4afa-9a5e-43adb78961eb",
        "name": "O-Genre",
        "description": None,
    },
    {
        "uuid": "7304f0fe-279d-46c3-a6c6-836f6ea03691",
        "name": "Y-Genre",
        "description": None,
    },
    {
        "uuid": "7ac3a58e-d652-4f6b-b103-e4f8ef9bbfd5",
        "name": "M-Genre",
        "description": "Some description M",
    },
    {
        "uuid": "880153c6-e1e3-4488-bfac-4b7b248a060a",
        "name": "J-Genre",
        "description": "Some description J",
    },
    {
        "uuid": "8ca53f1f-415a-4957-bf97-584706fd3942",
        "name": "U-Genre",
        "description": "Some description U",
    },
    {
        "uuid": "a04e4c9b-669d-41e7-bdfb-df0455b809ff",
        "name": "Q-Genre",
        "description": "Some description Q",
    },
    {
        "uuid": "a2c3fdd7-d724-4435-b8ce-986f541ce70e",
        "name": "K-Genre",
        "description": "Some description K",
    },
    {
        "uuid": "d00f8528-965b-446b-beb2-75e4acf976e3",
        "name": "G-Genre",
        "description": "Some description G",
    },
    {
        "uuid": "d0dc5363-c9d7-499f-8852-c6bc08045b6a",
        "name": "P-Genre",
        "description": "Some description P",
    },
    {
        "uuid": "da7bdf5c-8b83-42bb-b0c6-5f75f253be3e",
        "name": "Z-Genre",
        "description": None,
    },
]

list_genres_response_sort_map = {
    "uuid": sorted(
        list_genres_response,
        key=lambda item: item["uuid"],
    ),
    "-uuid": sorted(
        list_genres_response,
        key=lambda item: item["uuid"],
        reverse=True,
    ),
    "name": sorted(
        list_genres_response,
        key=lambda item: item["name"],
    ),
    "-name": sorted(
        list_genres_response,
        key=lambda item: item["name"],
        reverse=True,
    ),
}
