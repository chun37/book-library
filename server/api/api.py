from dataclasses import dataclass

from fastapi import FastAPI

from routes import health_check


@dataclass(frozen=True)
class FastAPIConfig:
    api_prefix: str = ""

    def asdict(self):
        return {}


@dataclass(frozen=True)
class Services:
    pass


class BooksAPI(FastAPI):
    def __init__(self, config: FastAPIConfig, services: Services):
        super().__init__(**config.asdict())
        self.include_router(
            health_check.Router(prefix=f"{config.api_prefix}/health_check")
        )
