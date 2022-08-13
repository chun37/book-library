from api import BooksAPI, FastAPIConfig, Services

cfg = FastAPIConfig()
services = Services()

app = BooksAPI(cfg, services)
