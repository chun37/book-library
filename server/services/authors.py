from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from models import Author, JsonAuthor
from repositories.authors import AuthorsRepositoryBase


class AuthorsServiceBase(ABC):
    @abstractmethod
    def add_author(self, author: Author) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_authors(self) -> list[Author]:
        raise NotImplementedError

    @abstractmethod
    def get_author(self, id: str) -> Optional[Author]:
        raise NotImplementedError


class AuthorsService(AuthorsServiceBase):
    def __init__(self, authors_repository: AuthorsRepositoryBase):
        self.authors_repository = authors_repository

    def add_author(self, author: Author) -> None:
        self.authors_repository.add_author(JsonAuthor.from_author(author))

    def get_authors(self) -> list[Author]:
        return [Author(a.id, a.name) for a in self.authors_repository.get_authors()]

    def get_author(self, id: str) -> Optional[Author]:
        authors = list(
            filter(lambda a: a.id == id, self.authors_repository.get_authors())
        )
        if len(authors) == 1:
            author = authors[0]
            return Author(author.id, author.name)
        return None
