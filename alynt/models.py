__all__ = (
    "Model",
    "User",
    "Anime",
)

from dataclasses import dataclass
from typing import List, TypeVar, Type
import dacite

T = TypeVar('T', bound="Model")


@dataclass
class Model:
    """Represents a generic model."""
    id_: int
    name: str

    @classmethod
    def from_dict(cls: Type[T], d: dict) -> T:
        return dacite.from_dict(dataclass=cls, data=d)


@dataclass
class User(Model):
    """Represents the User model."""


@dataclass
class Anime(Model):
    """Represents the Anime model."""
    author: str
    genres: List[str]
    synopsis: str
