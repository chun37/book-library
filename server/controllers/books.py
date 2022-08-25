from fastapi import HTTPException
from http import HTTPStatus
from behaviors import RegisterBook
from models import ISBN, Author, Book, CoverImage, JsonBook, Title
from services import Services


class Books:
    def __init__(self, services: Services):
        self.services = services

    def get(self) -> list[JsonBook]:
        return [JsonBook.from_book(b) for b in self.services.shelf_service.get_books()]

    def post(self, data: JsonBook) -> JsonBook:
        instance = RegisterBook(self.services.shelf_service)
        author = self.services.authors_service.get_author(data.author_id)
        if author is None:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST, detail="author not found."
            )
        b = Book(
            ISBN(data.isbn),
            Title(data.title),
            author,
            CoverImage(data.cover_image_url),
        )
        instance.handle(b)
        return JsonBook.from_book(b)
