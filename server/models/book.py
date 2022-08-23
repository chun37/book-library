from dataclasses import dataclass

from pydantic import BaseModel

from .author import Author
from .cover_image import CoverImage
from .isbn import ISBN
from .title import Title


@dataclass(frozen=True)
class Book:
    isbn: ISBN
    title: Title
    author: Author
    cover_image: CoverImage


class JsonBook(BaseModel):
    isbn: str
    title: str
    author_id: str
    cover_image_url: str

    @classmethod
    def from_book(cls, b: Book) -> "JsonBook":
        return cls(
            isbn=b.isbn.id,
            title=b.title.name,
            author_id=b.author.id,
            cover_image_url=b.cover_image.url,
        )
