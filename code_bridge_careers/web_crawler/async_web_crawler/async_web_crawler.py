from typing import Iterable
from aiohttp import ClientSession

from ..._typing import Optional, TracebackType, Literal, URL
from ._function import parse_http_response


class AsyncBaseWebCrawler:
    def __init__(self, timeout: int = 60, worker: int = 10, **headers):
        self.__timeout = timeout
        self.__worker = worker

        self.__session = ClientSession()

    async def fetch_one(
        self,
        url: URL,  # type: ignore
        text_or_json: Literal["text", "json"] = "text",  # noqa: F821
    ):
        async with self.__session.get(url) as response:
            return await parse_http_response(
                response=response,
                text_or_json=text_or_json,
            )

    async def fetch_many(
        self,
        urls: Iterable[URL],
        text_or_json: Literal["text", "json"] = "text",  # noqa: F821
    ):
        return (
            await self.fetch_one(url=url, text_or_json=text_or_json) for url in urls
        )

    def start(self):
        return self.__session

    async def close(self):
        await self.__session.close()

    async def __aenter__(self) -> ClientSession:
        return self.start()

    async def __aexit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ):
        await self.close()
