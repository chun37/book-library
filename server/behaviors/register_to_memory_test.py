# pylint: disable=duplicate-code
from models import ISBN, Book, Title
from repositories import InMemoryShelf
from services import ShelfService

from .register import RegisterBook


def test_本を登録する() -> None:
    shelf_repository = InMemoryShelf([])
    shelf_service = ShelfService(shelf_repository)
    book = Book(ISBN("1234567890"), Title("本のタイトル"))

    instance = RegisterBook(shelf_service)
    instance.handle(book)

    stock_books = instance.shelf.get_books()
    assert len(stock_books) == 1
    assert stock_books[0] == book
