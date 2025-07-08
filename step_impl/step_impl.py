# type: ignore
from getgauge.python import data_store, step
from hamcrest import assert_that, equal_to
from httpx import Response

from api.products import ProductsAPI


@step("Llamar al API de productos")
def call_to_products_api():
    fetched_products = ProductsAPI.get_products()
    data_store.scenario["products"] = fetched_products


@step("El status code de la respuesta debe ser <status_code>")
def validate_status_code(status_code: str):
    response: Response = data_store.scenario.get("products")
    assert_that(
        response.status_code,
        equal_to(int(status_code)),
        f"El código esperado ({status_code}) es diferente al obtenido ({response.status_code})",
    )
