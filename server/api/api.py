from dataclasses import dataclass
from typing import Any

from fastapi import FastAPI

from routes import books, health_check
from services import Services


@dataclass(frozen=True)
class FastAPIConfig:
    api_prefix: str = ""

    def as_dict(self) -> dict[str, Any]:
        return {
            "api_prefix": self.api_prefix,
        }


class BooksAPI(FastAPI):
    def __init__(self, config: FastAPIConfig, services: Services):
        super().__init__(**config.as_dict())  # type

        self.include_router(
            health_check.Router(prefix=f"{config.api_prefix}/health_check")
        )

        self.include_router(books.Router(services, prefix=f"{config.api_prefix}/books"))
