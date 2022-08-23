from abc import ABC, abstractmethod
from typing import Optional

from models import JsonAuthor


class AuthorsRepositoryBase(ABC):
    @abstractmethod
    def add_author(self, author: JsonAuthor) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_authors(self) -> list[JsonAuthor]:
        raise NotImplementedError

    @abstractmethod
    def get_author(self, id: str) -> Optional[JsonAuthor]:
        raise NotImplementedError
