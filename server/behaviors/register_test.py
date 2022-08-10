from repositories import InMemoryShelf
from models import ISBN, Book

from .register import RegisterBook


def test_本を登録する():
    shelf = InMemoryShelf([])
    book = Book(ISBN("1234567890"), "本のタイトル")

    instance = RegisterBook(shelf)
    instance.handle(book)

    assert instance.shelf.get_books()[book] == 1
