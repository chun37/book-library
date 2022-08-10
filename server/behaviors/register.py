from models import Book
from repositories import ShelfRepositoryBase


class RegisterBook:
    def __init__(self, shelf: ShelfRepositoryBase) -> None:
        self.shelf = shelf

    def handle(self, book: Book) -> None:
        self.shelf.add_book(book)
