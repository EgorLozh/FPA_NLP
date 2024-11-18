from dataclasses import dataclass, field

from src.domain.entities.base import BaseEntity


@dataclass
class Script(BaseEntity):
    name: str | None = None
    description: str | None = None
    request: Request | None = None
    actions: list[ScriptAction] = field(default_factory=list)


from src.domain.entities.request import Request
from src.domain.value_objects.script_action import ScriptAction
