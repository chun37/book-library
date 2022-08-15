from fastapi.testclient import TestClient

from api import BooksAPI, FastAPIConfig
from models import ISBN, Book, Title
from repositories import InMemoryShelf
from services import Services, ShelfService

cfg = FastAPIConfig(api_prefix="/api/v1")
services = Services(
    ShelfService(InMemoryShelf([Book(ISBN("0123456789"), Title("本の名前"))]))
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

    book = books[0]
    assert book["isbn"] == "0123456789"
    assert book["title"] == "本の名前"


def test_本が登録出来る() -> None:
    response = client.post(
        "/api/v1/books", json={"isbn": "0123456789", "title": "テスト本の名前"}
    )

    assert response.status_code == 201

    book = response.json()
    assert isinstance(book, dict)
    assert book["isbn"] == "0123456789"
    assert book["title"] == "テスト本の名前"


def test_存在しないところにアクセスすると404が返る() -> None:
    response = client.get("/api/v1/nothing_endpoint_404_hello")
    assert response.status_code == 404
    assert isinstance(response.json(), dict)
