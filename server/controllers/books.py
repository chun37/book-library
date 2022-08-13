from api_models import Book
from services import Services


class Books:
    def __init__(self, services: Services):
        self.services = services

    def get(self) -> list[Book]:
        return [
            Book(isbn=b.isbn.id, name=b.name)
            for b in self.services.shelf_service.get_books()
        ]
