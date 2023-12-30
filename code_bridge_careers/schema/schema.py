from multidict import CIMultiDictProxy
from pydantic import BaseModel

from .._typing import Any

__all__ = ["HttpJsonResponse", "HttpTextResponse"]


class HttpBaseResponse(BaseModel):
    status: int
    header: CIMultiDictProxy


class HttpJsonResponse(HttpBaseResponse):
    json: Any


class HttpTextResponse(HttpBaseResponse):
    html: str
