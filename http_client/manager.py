"""Browser manager module."""

import threading
from typing import Optional

import httpx


class ClientManager:
    """Class to manage the client instances."""

    _local = threading.local()

    @classmethod
    def set(cls, client: httpx.Client):
        """Assign a new client instance."""
        cls._local.instance = client

    @classmethod
    def client(cls) -> Optional[httpx.Client]:
        """Get the current client instance."""
        return getattr(cls._local, "instance", None)

    @classmethod
    def close(cls):
        """Close the current instance."""
        if hasattr(cls._local, "instance"):
            cls._local.instance.close()
            del cls._local.instance
