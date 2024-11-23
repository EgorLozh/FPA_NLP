from typing import Dict, Type

from src.domain.events.base import BaseEvent
from src.infra.broker.converter.strategies.base import BaseDictToEventStartegy, BaseEventToDictStrategy




class EventConverterMediator:
    event_to_dict_strategies: Dict[Type[BaseEvent], BaseEventToDictStrategy] = {}
    dict_to_event_strategies: Dict[Type[BaseEvent], BaseDictToEventStartegy] = {}

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(EventConverterMediator, cls).__new__(cls, *args, **kwargs)
        return cls.instance
    
    def register_event_to_dict_strategy(self, event_type: Type[BaseEvent], strategy: BaseEventToDictStrategy):
        self.event_to_dict_strategies[event_type] = strategy
    
    def register_dict_to_event_strategy(self, event_type: Type[BaseEvent], strategy: BaseDictToEventStartegy):
        self.dict_to_event_strategies[event_type] = strategy

    def get_event_to_dict_strategy(self, event_type: Type[BaseEvent]) -> BaseEventToDictStrategy:
        if event_type in self.event_to_dict_strategies:
            return self.event_to_dict_strategies[event_type]
        raise ValueError(f'Cant convert event to json. No strategy found for event {event_type}')
    
    def get_dict_to_event_strategy(self, event_type: Type[BaseEvent]) -> BaseDictToEventStartegy:
        if event_type in self.dict_to_event_strategies:
            return self.dict_to_event_strategies[event_type]
        raise ValueError(f'Cant convert json to event. No strategy found for event {event_type}')

