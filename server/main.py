import os

from api import BooksAPI, FastAPIConfig, Services
from database import get_client
from repositories.books import MongoBooksRepository
from repositories.authors import MongoAuthorsRepository
from services import ShelfService, AuthorsService

cfg = FastAPIConfig(api_prefix="/api/v1")
db = get_client(os.environ["MONGODB_URL"])
authors_repository = MongoAuthorsRepository(db)
books_repository = MongoBooksRepository(db)
services = Services(
    shelf_service=ShelfService(books_repository, authors_repository),
    authors_service=AuthorsService(authors_repository),
)

app = BooksAPI(cfg, services)
