from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID


@dataclass(eq=False)
class BaseEntity:
    oid: UUID = field(default_factory=UUID)
    created_at: datetime = field(default_factory=datetime.now)

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, self.__class__):
            return False
        return self.oid == value.oid
