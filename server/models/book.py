from dataclasses import dataclass

from .isbn import ISBN


@dataclass(frozen=True)
class Book:
    isbn: ISBN
    name: str
