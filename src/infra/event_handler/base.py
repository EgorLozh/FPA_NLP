from abc import ABC, abstractmethod
from src.domain.events.base import BaseEvent


class BaseEventHandler(ABC):
    @abstractmethod
    def __call__(self, event: BaseEvent) -> None:
        raise NotImplementedError