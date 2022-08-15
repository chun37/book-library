from dataclasses import dataclass

from .isbn import ISBN
from .title import Title


@dataclass(frozen=True)
class Book:
    isbn: ISBN
    title: Title
