from dataclasses import asdict

from fastapi import APIRouter

from api_models import Book
from controllers import Books
from services import Services

from .route import Route


class Router(APIRouter):
    def __init__(self, services: Services, *args, **kwargs):
        super().__init__(*args, **kwargs)

        books_controller = Books(services)
        paths = [
            Route("", books_controller.get, methods=["GET"], response_model=list[Book])
        ]

        for p in paths:  # pylint: disable=invalid-name
            self.add_api_route(**asdict(p))
