from dataclasses import dataclass
from src.domain.entities.script import Script
from src.domain.value_objects.video import Video
from src.domain.entities.base import BaseEntity


@dataclass
class Request(BaseEntity):
    video: Video
    script: Script
