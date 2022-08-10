from abc import ABC, abstractmethod
from collections import Counter

from models import Book
from repositories import ShelfRepositoryBase


class ShelfServiceBase(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_books(self) -> Counter:
        raise NotImplementedError


class ShelfService(ShelfServiceBase):
    def __init__(self, shelf_repository: ShelfRepositoryBase):
        self.shelf_repository = shelf_repository

    def add_book(self, book: Book) -> None:
        self.shelf_repository.add_book(book)

    def get_books(self) -> Counter:
        books = self.shelf_repository.get_books()
        return Counter(books)
