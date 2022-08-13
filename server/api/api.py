from dataclasses import asdict, dataclass

from fastapi import FastAPI
from routes import health_check


@dataclass(frozen=True)
class FastAPIConfig:
    pass

    def asdict(self):
        return {}


@dataclass(frozen=True)
class Services:
    pass


class BooksAPI(FastAPI):
    def __init__(self, config: FastAPIConfig, services: Services):
        super().__init__(**config.asdict())
        self.include_router(health_check.Router(prefix="/api/v1/health_check"))
