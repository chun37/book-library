from fastapi import FastAPI
from dataclasses import dataclass, asdict


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
