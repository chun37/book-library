from typing import Any

from fastapi import APIRouter

from controllers import Books
from models import JsonBook
from services import Services

from .route import Route


class Router(APIRouter):
    def __init__(
        self,
        services: Services,
        prefix: str,
        *args: list[Any],
        **kwargs: dict[str, Any]
    ):
        super().__init__(prefix=prefix, *args, **kwargs)  # type: ignore

        books_controller = Books(services)
        paths = [
            Route(
                "", books_controller.get, methods=["GET"], response_model=list[JsonBook]
            ),
            Route(
                "",
                books_controller.post,
                methods=["POST"],
                response_model=JsonBook,
                status_code=201,
            ),
        ]

        for p in paths:  # pylint: disable=invalid-name
            self.add_api_route(**p.as_dict())
