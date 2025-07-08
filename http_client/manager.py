"""Browser manager module."""

import threading

import httpx


class ClientManager:
    """Class to manage the client instances."""

    _local = threading.local()

    @classmethod
    def set(cls, client: httpx.Client):
        """Assign a new client instance."""
        cls._local.instance = client

    @classmethod
    def client(cls) -> httpx.Client:
        """Get the current client instance, or fail fast if not initialized."""
        client = getattr(cls._local, "instance", None)
        if client is None:
            raise RuntimeError("HTTP client has not been initialized in this thread.")
        return client

    @classmethod
    def close(cls):
        """Close the current instance."""
        if hasattr(cls._local, "instance"):
            cls._local.instance.close()
            del cls._local.instance
