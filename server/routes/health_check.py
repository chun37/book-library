from dataclasses import asdict

from fastapi import APIRouter

from controllers import HealthCheck

from .route import Route


class Router(APIRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        health_check_controller = HealthCheck()
        paths = [Route("", health_check_controller.get, methods=["GET"])]

        for p in paths:  # pylint: disable=invalid-name
            self.add_api_route(**asdict(p))
