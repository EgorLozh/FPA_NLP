from typing import Dict, List

from src.domain.events.base import BaseEvent, BaseEventHandler


class MessageBus:
    event_handlers: Dict[BaseEvent, List[BaseEventHandler]] = {}

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MessageBus, cls).__new__(cls)
        return cls.instance
    
    def register(self, event: BaseEvent, handler: BaseEventHandler):
        if event not in self.event_handlers:
            self.event_handlers[event] = [handler]
        self.event_handlers[event].append(handler)

    def handle(self, event: BaseEvent):
        if event not in self.event_handlers:
            raise ValueError(f'Event {event} not registered')
        
        results = [handler(event) for handler in self.event_handlers[event]]
        return results
