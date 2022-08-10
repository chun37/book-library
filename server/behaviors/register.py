from models import Book
from services import ShelfServiceBase


class RegisterBook:
    def __init__(self, shelf: ShelfServiceBase) -> None:
        self.shelf = shelf

    def handle(self, book: Book) -> None:
        self.shelf.add_book(book)
