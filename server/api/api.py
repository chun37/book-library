from dataclasses import dataclass

from fastapi import FastAPI

from routes import books, health_check
from services import Services


@dataclass(frozen=True)
class FastAPIConfig:
    api_prefix: str = ""


class BooksAPI(FastAPI):
    def __init__(self, config: FastAPIConfig, services: Services):
        super().__init__(**config.asdict())

        self.include_router(
            health_check.Router(prefix=f"{config.api_prefix}/health_check")
        )

        self.include_router(books.Router(services, prefix=f"{config.api_prefix}/books"))
