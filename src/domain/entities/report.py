from dataclasses import dataclass

from src.domain.entities.base import BaseEntity


@dataclass
class Report(BaseEntity):
    marks: list[Mark]

    @property
    def complited_persent(self) -> float:
        pass

    @property
    def total_score(self) -> int:
        pass

from src.domain.value_objects.mark import Mark
