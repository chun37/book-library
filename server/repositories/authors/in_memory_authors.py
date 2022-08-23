from typing import Optional

from models import JsonAuthor

from .authors import AuthorsRepositoryBase


class InMemoryAuthorsRepository(AuthorsRepositoryBase):
    def __init__(self, authors: list[JsonAuthor]):
        self._authors = authors

    def add_author(self, author: JsonAuthor) -> None:
        self._authors.append(author)

    def get_author(self, id: str) -> Optional[JsonAuthor]:
        selected_author = list(filter(lambda a: a.id, self._authors))
        if len(selected_author) != 1:
            return None
        return selected_author[0]

    def get_authors(self) -> list[JsonAuthor]:
        return self._authors
