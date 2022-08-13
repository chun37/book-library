from fastapi import APIRouter

from api_models import Book as JsonBook
from controllers import Books
from services import Services

from .route import Route


class Router(APIRouter):
    def __init__(self, services: Services, *args, **kwargs):
        super().__init__(*args, **kwargs)

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
