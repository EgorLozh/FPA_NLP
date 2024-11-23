from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class BaseEvent:
    pass


class BaseEventHandler(ABC):
    @abstractmethod
    def __call__(self, event: BaseEvent) -> None:
        raise NotImplementedError
