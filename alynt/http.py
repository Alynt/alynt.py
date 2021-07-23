from functools import partialmethod
from typing import Any, Optional

from aiohttp import ClientSession

from . import models


class HTTPClient:
    __slots__ = (
        "token",
        "session",
    )

    def __init__(self,
                 token: str,
                 session: Optional[ClientSession] = None) -> None:

        self.token = token

        if session is None:
            session = ClientSession()

        self.session = session
        self._closed = False

    def is_closed(self) -> bool:
        return self._closed

    async def close(self) -> None:
        if self._closed:
            return

        try:
            await self.session.close()
        finally:
            self.session = None

        self._closed = True

    async def request(self, method: str, route: str, **parameters: Any) -> Any:
        pass

    get     = partialmethod(request, "GET")
    post    = partialmethod(request, "POST")
    patch   = partialmethod(request, "PATCH")
    delete  = partialmethod(request, "DELETE")

    async def get_anime(
        self,
        name: Optional[str] = None, /,
        id: Optional[int] = None
    ) -> models.Anime:
        pass

    async def get_user(self, id: int) -> models.User:
        pass
