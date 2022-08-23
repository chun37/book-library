from dataclasses import asdict
from typing import Any

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.cursor import Cursor

from models import ISBN, Author, CoverImage, Title, JsonBook

from .books import BooksRepositoryBase


class MongoBooksRepository(BooksRepositoryBase):
    def __init__(self, client: MongoClient) -> None:
        self.collection = client["library"]["books"]

    def add_book(self, book: JsonBook) -> None:
        self.collection.insert_one(book.dict())

    def get_books(self) -> list[JsonBook]:
        return [
            JsonBook(
                isbn=c["isbn"],
                title=c["title"],
                author_id=c["author_id"],
                cover_image_url=c["cover_image_url"],
            )
            for c in self.collection.find()
        ]
