from fastapi.testclient import TestClient

from repositories import InMemoryShelf
from services import Services, ShelfService
from api import BooksAPI, FastAPIConfig

cfg = FastAPIConfig(api_prefix="/api/v1")
services = Services(ShelfService(InMemoryShelf([])))

client = TestClient(BooksAPI(cfg, services))


def test_APIが動いている():
    response = client.get("/api/v1/health_check")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_本の一覧が見れる():
    response = client.get("/api/v1/books")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_本が登録出来る():
    response = client.get("/api/v1/books/BOOK_ID")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_存在しないところにアクセスすると404が返る():
    response = client.get("/api/v1/nothing_endpoint_404_hello")
    assert response.status_code == 404
    assert isinstance(response.json(), dict)
