from aiohttp import ClientSession

from ..._typing import Any, AsyncGenerator

__all__ = ["get_aiohttp_async_session"]


async def get_aiohttp_async_session() -> AsyncGenerator[ClientSession, Any]:
    async with ClientSession() as async_session:
        yield async_session
