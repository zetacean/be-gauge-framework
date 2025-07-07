# type: ignore

from getgauge.python import DataStore, before_spec, step

from api.products import ProductsAPI
from constants import DEFAULT_URL
from http_client.builder import HttpClientBuilder
from http_client.manager import ClientManager

data = DataStore()


@before_spec
def before_spec_hook():
    client = (
        HttpClientBuilder()
        .with_base_url(DEFAULT_URL)
        .with_headers({"content-type": "application/json"})
        .build()
    )
    ClientManager.set(client)


@step("Make a simple request")
def make_a_simple_request():
    test = ProductsAPI.get_products()
    data.put("products", test)
    print(test)
