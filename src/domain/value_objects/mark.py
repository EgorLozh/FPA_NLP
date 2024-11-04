from dataclasses import dataclass

from src.domain.value_objects.base import BaseValueObject


@dataclass
class Mark(BaseValueObject):
    check: bool
    report: Report
    script_action: ScriptAction

from src.domain.entities.report import Report
from src.domain.value_objects.script_action import ScriptAction