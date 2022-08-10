from dataclasses import dataclass


@dataclass(frozen=True)
class ISBN:
    id: str

    def __post__init__(self) -> None:
        if len(self.id) not in [10, 13]:
            raise ValueError("ISBNは10桁か13桁である必要があります")
