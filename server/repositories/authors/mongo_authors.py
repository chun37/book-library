from typing import Optional

from pymongo import MongoClient

from models import JsonAuthor

from .authors import AuthorsRepositoryBase


class MongoAuthorsRepository(AuthorsRepositoryBase):
    def __init__(self, client: MongoClient) -> None:
        self.collection = client["library"]["authors"]

    def add_author(self, author: JsonAuthor) -> None:
        self.collection.insert_one(author.dict())

    def get_author(self, id: str) -> Optional[JsonAuthor]:
        return self.collection.find_one({"id": id})

    def get_authors(self) -> list[JsonAuthor]:
        return list(self.collection.find())
