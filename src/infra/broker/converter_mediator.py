from typing import Dict, Type

from src.domain.events.base import BaseEvent
from src.infra.broker.strategies.base import BaseEventToDictStrategy, BaseDictToEventStartegy

class ConverterMediator:
    dict_to_event_strategies: Dict[str, BaseDictToEventStartegy]
    event_to_dict_strategies: Dict[Type[BaseEvent], BaseEventToDictStrategy]

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ConverterMediator, cls).__new__(cls)
        return cls.instance
    
    def register_dict_to_event_strategy(self, event_type: str, strategy: BaseDictToEventStartegy):
        self.dict_to_event_strategies[event_type] = strategy

    def register_event_to_dict_strategy(self, event_type: Type[BaseEvent], strategy: BaseEventToDictStrategy):
        self.event_to_dict_strategies[event_type] = strategy

    def dict_to_event(self, json: dict) -> BaseEvent:
        event_type = json['type']
        if event_type not in self.dict_to_event_strategies:
            raise Exception(f'No strategy found for type {event_type}') 
        return self.dict_to_event_strategies[event_type].dict_to_event(json)
    
    def event_to_dict(self, event: BaseEvent) -> dict:
        if event.__class__ not in self.event_to_dict_strategies:
            raise Exception(f'No strategy found for type {event.__class__}') 
        return self.event_to_dict_strategies[event.__class__].event_to_dict(event)
