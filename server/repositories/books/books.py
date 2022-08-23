from abc import ABC, abstractmethod

from models import Book, JsonBook


class BooksRepositoryBase(ABC):
    @abstractmethod
    def add_book(self, book: JsonBook) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_books(self) -> list[JsonBook]:
        raise NotImplementedError
