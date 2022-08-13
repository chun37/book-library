import os

from api import BooksAPI, FastAPIConfig, Services
from database import get_client
from repositories import MongoShelf
from services import ShelfService

cfg = FastAPIConfig(api_prefix="/api/v1")
services = Services(
    shelf_service=ShelfService(MongoShelf(get_client(os.environ["MONGODB_URL"])))
)

app = BooksAPI(cfg, services)
