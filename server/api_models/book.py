from pydantic import BaseModel


class Book(BaseModel):
    isbn: str
    name: str
