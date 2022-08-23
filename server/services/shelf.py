from abc import ABC, abstractmethod

from models import Book, JsonBook, ISBN, CoverImage, Title
from repositories.books import BooksRepositoryBase
from repositories.authors import AuthorsRepositoryBase


class ShelfServiceBase(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_books(self) -> list[Book]:
        raise NotImplementedError


class ShelfService(ShelfServiceBase):
    def __init__(
        self,
        shelf_repository: BooksRepositoryBase,
        author_repository: AuthorsRepositoryBase,
    ):
        self.shelf_repository = shelf_repository
        self.author_repository = author_repository

    def add_book(self, book: Book) -> None:
        jb = JsonBook.from_book(book)
        self.shelf_repository.add_book(jb)

    def get_books(self) -> list[Book]:
        books = self.shelf_repository.get_books()
        return [
            Book(
                ISBN(b.isbn),
                Title(b.title),
                self.author_repository.get_author(b.author_id),
                CoverImage(b.cover_image_url),
            )
            for b in books
        ]
