from models import ISBN, Book
from mongomock import MongoClient
from repositories import MongoShelf
from services import ShelfService

from .register import RegisterBook


def test_本を登録する() -> None:
    shelf_repository = MongoShelf(MongoClient()["library"])
    shelf_service = ShelfService(shelf_repository)
    book = Book(ISBN("1234567890"), "本のタイトル")

    instance = RegisterBook(shelf_service)
    instance.handle(book)

    assert instance.shelf.get_books()[book] == 1