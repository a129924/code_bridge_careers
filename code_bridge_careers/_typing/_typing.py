from typing import (
    Any,
    AsyncGenerator,
    Union,
    Optional,
    Literal,
    Iterable,
    TypeVar,
)
from types import TracebackType

__all__ = [
    "Any",
    "AsyncGenerator",
    "Union",
    "Optional",
    "TracebackType",
    "Literal",
    "Iterable",
    "URL",
]


URL = TypeVar("URL", bound=str)
