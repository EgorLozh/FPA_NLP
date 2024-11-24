from typing import Dict, List, Type

from src.domain.events.base import BaseEvent, BaseEventHandler


class MessageBus:
    event_handlers: Dict[Type[BaseEvent], List[BaseEventHandler]] = {}

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MessageBus, cls).__new__(cls)
        return cls.instance
    
    def register(self, event_type: Type[BaseEvent], handler: BaseEventHandler):
        if event_type not in self.event_handlers:
            self.event_handlers[event_type] = [handler]
        if handler not in self.event_handlers[event_type]:
            self.event_handlers[event_type].append(handler)

    def handle(self, event: BaseEvent):
        if event.__class__ not in self.event_handlers:
            raise ValueError(f'Handler for {event.__class__} not found')
        
        results = [handler(event) for handler in self.event_handlers[event.__class__]]
        return results
