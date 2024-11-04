from dataclasses import dataclass

from src.domain.value_objects.base import BaseValueObject


@dataclass
class ScriptAction(BaseValueObject):
    text: str
    script: Script
    weight: int


from src.domain.entities.script import Script
