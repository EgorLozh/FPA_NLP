from dataclasses import dataclass, field
from src.domain.entities.base import BaseEntity
from src.domain.value_objects.video import Video
from src.domain.entities.script import Script


@dataclass
class Request(BaseEntity):
    video: Video = field(kw_only=True)
    script: Script = field(kw_only=True)
