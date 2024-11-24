from infra.broker.converter_mediator import ConverterMediator
from src.domain.events.base import BaseEvent
from src.infra.broker.base import BaseBrokerClient


class Publisher(BaseBrokerClient):
    converter_mediator = ConverterMediator()

    def publish(self, event: BaseEvent):
        if not self.channel:
            self.connect()

        message = self.converter_mediator.event_to_dict(event)

        self.channel.basic_publish(exchange='', routing_key=self.queue, body=message)
    