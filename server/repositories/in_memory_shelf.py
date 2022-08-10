from collections import Counter

from models import Book
from .shelf import ShelfRepositoryBase


class InMemoryShelf(ShelfRepositoryBase):
    def __init__(self, shelf: list[Book]):
        self._shelf = shelf

    def add_book(self, book: Book) -> None:
        self._shelf.append(book)
        return None

    def get_books(self) -> Counter:
        return Counter(self._shelf)
