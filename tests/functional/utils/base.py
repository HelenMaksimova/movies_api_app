from collections.abc import Callable
from http import HTTPMethod

from aiohttp import ClientSession

__all__ = ("TestBase",)


class TestBase:
    BASE_URL: str | None = None
    API_URL: str | None = None
    METHOD: str = HTTPMethod.GET
    ELASTIC_INDEX: str | None = None
    _session: ClientSession | None = None

    @property
    def request_map(self) -> dict[str, Callable]:
        return {
            HTTPMethod.GET: self._get_request,
            HTTPMethod.POST: self._post_request,
        }

    @classmethod
    @property
    def session(cls) -> ClientSession:
        if cls._session is None or cls._session.closed:
            cls._session = ClientSession()
        return cls._session

    @classmethod
    async def _session_close(cls) -> None:
        if cls._session and not cls._session.closed:
            await cls._session.close()

    @property
    def api_url(self) -> str:
        if self.BASE_URL and self.API_URL:
            return f"http://{self.BASE_URL}/{self.API_URL}"

        raise ValueError("BASE_URL and API_URL must be defined")

    async def _get_request(
        self,
        url: str,
        headers: dict | None = None,
        cookies: dict | None = None,
        params: dict | None = None,
    ) -> tuple[dict, dict, int]:
        async with self.session.get(
            url, headers=headers, cookies=cookies, params=params
        ) as response:
            body = await response.json()
            headers = response.headers
            status = response.status

        return body, headers, status

    async def _post_request(
        self,
        url: str,
        headers: dict | None = None,
        cookies: dict | None = None,
        params: dict | None = None,
    ) -> tuple[dict, dict, int]:
        async with self.session.post(
            url, headers=headers, cookies=cookies, json=params
        ) as response:
            body = await response.json()
            headers = response.headers
            status = response.status

        return body, headers, status

    async def request(
        self,
        url: str | None = None,
        method: str | None = None,
        body: dict | None = None,
        headers: dict | None = None,
        cookies: dict | None = None,
        **query_params,
    ) -> tuple[dict, dict, int]:
        request_url = url or self.api_url
        request_method = method or self.METHOD
        params = query_params or body

        request = self.request_map.get(request_method)
        if request:
            return await request(
                request_url, headers=headers, cookies=cookies, params=params
            )
        else:
            raise ValueError(f"Unsupported request method: {request_method}")
