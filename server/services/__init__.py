from dataclasses import dataclass

from .authors import AuthorsService, AuthorsServiceBase
from .shelf import ShelfService, ShelfServiceBase


@dataclass(frozen=True)
class Services:
    shelf_service: ShelfService
    authors_service: AuthorsService
