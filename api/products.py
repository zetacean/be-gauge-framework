from httpx import Response

from http_client.manager import ClientManager


class ProductsAPI:

    @staticmethod
    def get_products() -> Response:

        return ClientManager.client().get("/products")
