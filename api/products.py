from http_client.manager import ClientManager


class ProductsAPI:

    @staticmethod
    def get_products():
        return ClientManager.client().get("/products").json()
