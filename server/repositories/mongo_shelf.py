from dataclasses import asdict

from models import ISBN, Book
from pymongo import MongoClient
from pymongo.collection import Collection

from .shelf import ShelfRepositoryBase


class MongoShelf(ShelfRepositoryBase):
    def __init__(self, client: MongoClient) -> None:
        self.collection: Collection[Book] = client["library"]["shelf"]

    def add_book(self, book: Book) -> None:
        self.collection.insert_one(asdict(book))

    def get_books(self) -> list[Book]:
        books: list[Book] = list(self.collection.find())
        # データベースのID類は不必要なので、オブジェクトを再生成している
        return [Book(ISBN(**b["isbn"]), b["name"]) for b in books]
