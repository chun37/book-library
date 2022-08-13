from api import BooksAPI, FastAPIConfig, Services

cfg = FastAPIConfig()
services = Services()

app = BooksAPI(cfg, services)


@app.get("/")
async def root():
    return {"message": "Hello World"}
