from dataclasses import dataclass

from src.domain.value_objects.base import BaseValueObject
from src.domain.entities.script import Script


@dataclass
class ScriptAction(BaseValueObject):
    text: str
    weight: int
    script: Script


