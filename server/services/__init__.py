from dataclasses import dataclass

from .shelf import ShelfService, ShelfServiceBase


@dataclass(frozen=True)
class Services:
    shelf_service: ShelfService
