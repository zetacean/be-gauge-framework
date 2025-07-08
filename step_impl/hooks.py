# type: ignore

from getgauge.python import before_spec

from constants import DEFAULT_URL
from http_client.builder import HttpClientBuilder
from http_client.manager import ClientManager


@before_spec
def before_spec_hook():
    client = (
        HttpClientBuilder()
        .with_base_url(DEFAULT_URL)
        .with_headers({"content-type": "application/json"})
        .build()
    )
    ClientManager.set(client)
