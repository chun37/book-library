from models import Book
from services import Services


class Books:
    def __init__(self, services: Services):
        self.services = services

    def get(self) -> list[Book]:
        return self.services.shelf_service.get_books()
