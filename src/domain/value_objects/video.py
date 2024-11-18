from dataclasses import dataclass
from src.domain.value_objects.base import BaseValueObject


@dataclass
class Video(BaseValueObject):
    url: str
    file_name: str | None = None
    speech: str | None = None
    request: Request | None = None

from src.domain.entities.request import Request
