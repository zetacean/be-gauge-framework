# type: ignore
from decouple import config

DEFAULT_URL: str = config("base_url", cast=str)
