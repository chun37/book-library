from abc import ABC, abstractmethod
from collections import Counter

from models import Book


class ShelfRepositoryBase(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_books(self) -> Counter:
        raise NotImplementedError
