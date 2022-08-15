from pydantic import BaseModel

from models import Book


class JsonBook(BaseModel):
    isbn: str
    title: str

    @classmethod
    def from_book(cls, b: Book) -> "JsonBook":
        return cls(isbn=b.isbn.id, title=b.title.name)
