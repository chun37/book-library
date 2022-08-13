from dataclasses import asdict

from fastapi import APIRouter

from controllers import health_check

from .route import Route

paths = [Route("", health_check.get, methods=["GET"])]


class Router(APIRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for p in paths:
            self.add_api_route(**asdict(p))
