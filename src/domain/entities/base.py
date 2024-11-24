from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4


@dataclass(eq=False)
class BaseEntity:
    oid: str = field(
        default_factory=lambda: str(uuid4()),
        kw_only=True,
    )
    created_at: datetime = field(default_factory=datetime.now)

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, self.__class__):
            return False
        return self.oid == value.oid
