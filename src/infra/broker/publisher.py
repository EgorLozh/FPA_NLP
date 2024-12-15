import json
import pika

from src.infra.broker.converter_mediator import ConverterMediator
from src.domain.events.base import BaseEvent
from src.infra.broker.base import BaseBrokerClient


class Publisher(BaseBrokerClient):
    converter_mediator = ConverterMediator()

    def publish(self, event: BaseEvent):
        try:
            if not self.channel or self.channel.is_closed:
                self.connect()

            message = self.converter_mediator.event_to_dict(event)
            message = json.dumps(message)

            self.channel.basic_publish(exchange='', routing_key=self.queue, body=message)
        except pika.exceptions.ConnectionClosed as e:
            self.reconnect()
    