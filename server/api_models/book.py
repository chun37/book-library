from pydantic import BaseModel

from models import Book as DomainBook


class Book(DomainBook, BaseModel):
    pass
