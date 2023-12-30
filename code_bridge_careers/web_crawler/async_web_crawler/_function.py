from aiohttp import ClientResponse

from ...schema import HttpTextResponse, HttpJsonResponse
from ..._typing import Literal, Union


async def parse_http_response(
    response: ClientResponse,
    text_or_json: Literal["text", "json"],  # noqa: F821
) -> Union[HttpJsonResponse, HttpTextResponse]:
    # assert response.status == 200

    return (
        HttpTextResponse(
            status=response.status,
            header=response.headers,
            html=await response.text(),
        )
        if text_or_json == "text"
        else HttpJsonResponse(
            status=response.status,
            header=response.headers,
            json=response.json(),
        )
    )
