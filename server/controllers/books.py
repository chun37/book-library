from api_models import Book as JsonBook
from behaviors import RegisterBook
from models import ISBN, Book
from services import Services


class Books:
    def __init__(self, services: Services):
        self.services = services

    def get(self) -> list[JsonBook]:
        return [
            JsonBook(isbn=b.isbn.id, name=b.name)
            for b in self.services.shelf_service.get_books()
        ]

    def post(self, data: JsonBook) -> JsonBook:
        instance = RegisterBook(self.services.shelf_service)
        b = Book(ISBN(data.isbn), data.name)
        instance.handle(b)
        return JsonBook(isbn=b.isbn.id, name=b.name)
