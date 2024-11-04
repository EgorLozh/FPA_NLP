from dataclasses import dataclass, field

from src.domain.entities.base import BaseEntity


@dataclass
class Script(BaseEntity):
    name: str | None = field(default=None)
    description: str | None = field(default=None)
    actions: list[ScriptAction] = field(default_factory=list)


from src.domain.value_objects.script_action import ScriptAction
