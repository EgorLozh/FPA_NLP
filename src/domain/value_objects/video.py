from dataclasses import dataclass
from typing import Optional
from src.domain.value_objects.base import BaseValueObject


@dataclass
class Video(BaseValueObject):
    url: str
    file_name: str | None = None
    speech: str | None = None
    request: Optional['Request'] = None

