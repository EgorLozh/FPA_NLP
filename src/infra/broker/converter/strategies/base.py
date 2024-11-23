from abc import ABC, abstractmethod

from src.domain.events.base import BaseEvent



class BaseDictToEventStartegy(ABC):
    @staticmethod
    @abstractmethod
    def dict_to_event(json: dict) -> BaseEvent:
        pass


class BaseEventToDictStrategy(ABC):
    @staticmethod
    @abstractmethod
    def event_to_dict(event: BaseEvent) -> dict:
        pass
