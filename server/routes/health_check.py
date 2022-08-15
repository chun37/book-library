from typing import Any

from fastapi import APIRouter

from controllers import HealthCheck

from .route import Route


class Router(APIRouter):
    def __init__(self, prefix: str, *args: list[Any], **kwargs: dict[str, Any]) -> None:
        super().__init__(prefix=prefix, *args, **kwargs)  # type: ignore

        health_check_controller = HealthCheck()
        paths = [Route("", health_check_controller.get, methods=["GET"])]

        for p in paths:  # pylint: disable=invalid-name
            self.add_api_route(**p.as_dict())
