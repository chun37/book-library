from api_models import JsonBook
from behaviors import RegisterBook
from models import ISBN, Book, Title
from services import Services


class Books:
    def __init__(self, services: Services):
        self.services = services

    def get(self) -> list[JsonBook]:
        return [JsonBook.from_book(b) for b in self.services.shelf_service.get_books()]

    def post(self, data: JsonBook) -> JsonBook:
        instance = RegisterBook(self.services.shelf_service)
        b = Book(ISBN(data.isbn), Title(data.title))
        instance.handle(b)
        return JsonBook.from_book(b)
