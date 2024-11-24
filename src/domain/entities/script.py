from typing import Optional, List
from dataclasses import dataclass, field

from src.domain.entities.base import BaseEntity


@dataclass
class Script(BaseEntity):
    request: Optional['Request'] = None
    actions: List['ScriptAction'] = field(default_factory=list)
