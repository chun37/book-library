from dataclasses import dataclass


@dataclass(frozen=True)
class CoverImage:
    url: str = "https://placehold.jp/ababab/000000/200x280.png?text=No%20Image"
