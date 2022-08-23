from models import Book, JsonBook, ISBN, Title

from .books import BooksRepositoryBase


class InMemoryBooksRepository(BooksRepositoryBase):
    def __init__(self, shelf: list[JsonBook]):
        self._shelf = shelf

    def add_book(self, book: JsonBook) -> None:
        self._shelf.append(book)

    def get_books(self) -> list[JsonBook]:
        return self._shelf
