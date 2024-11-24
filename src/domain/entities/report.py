from typing import List
from dataclasses import dataclass, field

from src.domain.entities.request import Request
from src.domain.entities.base import BaseEntity


@dataclass
class Report(BaseEntity):
    marks: List['Mark'] = field(default_factory=list)
    request: Request = field(kw_only=True)

    @property
    def complited_persent(self) -> float:
        return len(filter(lambda mark: mark.check, self.marks)) / len(self.marks)

    @property
    def total_score(self) -> int:
        return sum([mark.script_action.weight if mark.check else 0 for mark in self.marks])

from src.domain.value_objects.mark import Mark
