from abc import ABC, abstractmethod

from models import Book


class ShelfRepositoryBase(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_books(self) -> list[Book]:
        raise NotImplementedError
