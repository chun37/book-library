from uuid import uuid4

from fastapi.testclient import TestClient

from api import BooksAPI, FastAPIConfig
from models import ISBN, Author, Book, CoverImage, Title, JsonAuthor, JsonBook
from repositories.books import InMemoryBooksRepository
from repositories.authors import InMemoryAuthorsRepository
from services import Services, ShelfService, AuthorsService

cfg = FastAPIConfig(api_prefix="/api/v1")
author_id = uuid4().hex

authors_repository = InMemoryAuthorsRepository(
    [
        JsonAuthor(id=author_id, name="著者の名前"),
    ]
)
books_repository = InMemoryBooksRepository(
    [
        JsonBook(
            isbn="1234567890",
            title="本のタイトル",
            author_id=author_id,
            cover_image_url="https://placehold.jp/ababab/000000/200x280.png?text=No%20Image",
        )
    ]
)

services = Services(
    ShelfService(books_repository, authors_repository),
    AuthorsService(authors_repository),
)

client = TestClient(BooksAPI(cfg, services))


def test_APIが動いている() -> None:
    response = client.get("/api/v1/health_check")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_本の一覧が見れる() -> None:
    response = client.get("/api/v1/books")
    books = response.json()

    assert response.status_code == 200
    assert isinstance(books, list)

    assert len(books) == 1
    book = books[0]
    assert book["isbn"] == "1234567890"
    assert book["title"] == "本のタイトル"
    assert book["author_id"] == author_id
    assert (
        book["cover_image_url"]
        == "https://placehold.jp/ababab/000000/200x280.png?text=No%20Image"
    )


def test_著者の存在する本が登録出来る() -> None:
    response = client.post(
        "/api/v1/books",
        json={
            "isbn": "0123456789",
            "title": "テスト本の名前",
            "author_id": author_id,
            "cover_image_url": "https://cover.openbd.jp/9784040647777.jpg",
        },
    )

    assert response.status_code == 201

    book = response.json()
    assert isinstance(book, dict)
    assert book["isbn"] == "0123456789"
    assert book["title"] == "テスト本の名前"
    assert book["author_id"] == author_id
    assert book["cover_image_url"] == "https://cover.openbd.jp/9784040647777.jpg"


def test_著者の存在しない本が登録出来る() -> None:
    response = client.post(
        "/api/v1/books",
        json={
            "isbn": "0123456789",
            "title": "テスト本の名前",
            "author_id": uuid4().hex,
            "cover_image_url": "https://cover.openbd.jp/9784040647777.jpg",
        },
    )
    assert response.status_code == 400


def test_存在しないところにアクセスすると404が返る() -> None:
    response = client.get("/api/v1/nothing_endpoint_404_hello")
    assert response.status_code == 404
    assert isinstance(response.json(), dict)
