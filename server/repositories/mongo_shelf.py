from dataclasses import asdict

from pymongo import MongoClient
from pymongo.collection import Collection

from models import ISBN, Book, Title

from .shelf import ShelfRepositoryBase


class MongoShelf(ShelfRepositoryBase):
    def __init__(self, client: MongoClient) -> None:
        self.collection = client["library"]["shelf"]

    def add_book(self, book: Book) -> None:
        self.collection.insert_one(asdict(book))

    def get_books(self) -> list[Book]:
        books: list[dict[str, dict[str, str]]] = list(self.collection.find())
        # データベースのID類は不必要なので、オブジェクトを再生成している
        return [Book(ISBN(**b["isbn"]), Title(**b["title"])) for b in books]
