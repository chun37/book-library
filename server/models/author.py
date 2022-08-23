from dataclasses import dataclass

from pydantic import BaseModel


@dataclass(frozen=True)
class Author:
    id: str
    name: str


class JsonAuthor(BaseModel):
    id: str
    name: str

    @classmethod
    def from_author(cls, author: Author) -> "JsonAuthor":
        return cls(id=author.id, name=author.name)
