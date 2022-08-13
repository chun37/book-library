from api import BooksAPI, FastAPIConfig, Services

cfg = FastAPIConfig(api_prefix="/api/v1")
services = Services()

app = BooksAPI(cfg, services)
