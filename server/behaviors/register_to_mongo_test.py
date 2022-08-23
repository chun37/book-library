# pylint: disable=duplicate-code
from uuid import uuid4

from mongomock import MongoClient

from models import ISBN, Author, Book, CoverImage, Title
from repositories.books import MongoBooksRepository
from repositories.authors import InMemoryAuthorsRepository
from services import ShelfService

from .register import RegisterBook


def test_本を登録する() -> None:
    author_id = uuid4().hex
    shelf_repository = MongoBooksRepository(MongoClient())

    authors_repository = InMemoryAuthorsRepository([Author(author_id, "著者の名前")])
    shelf_service = ShelfService(shelf_repository, authors_repository)

    book = Book(
        ISBN("1234567890"), Title("本のタイトル"), Author(author_id, "著者の名前"), CoverImage()
    )

    instance = RegisterBook(shelf_service)
    instance.handle(book)

    stock_books = instance.shelf.get_books()
    assert len(stock_books) == 1
    assert stock_books[0] == book
