from abc import ABC
from typing import Self

import httpx


class HttpClientBuilder(ABC):
    _base_url: str
    _headers: dict[str, str]
    _timeout: int = 5
    _verify: bool = True

    def with_base_url(self, base_url: str) -> Self:
        self._base_url = base_url
        return self

    def with_headers(self, headers: dict[str, str]) -> Self:
        self._headers = headers
        return self

    def with_timeout(self, timeout: int) -> Self:
        self._timeout = timeout
        return self

    def with_ssl_verification(self, verify: bool) -> Self:
        self._verify = verify
        return self

    def build(self) -> httpx.Client:
        return httpx.Client(
            base_url=self._base_url,
            headers=self._headers,
            timeout=self._timeout,
            verify=self._verify,
        )
