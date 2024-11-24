import json

from src.infra.services.logger_service import LoggerService
from src.infra.broker.converter_mediator import ConverterMediator
from src.domain.events.base import BaseEvent
from src.infra.broker.base import BaseBrokerClient
from src.infra.message_bus import MessageBus


class Consumer(BaseBrokerClient):
    logger = LoggerService()
    message_bus = MessageBus()
    converter_mediator = ConverterMediator()

    def call_back(self, ch, method, properties, body):

        json_str = body.decode('utf-8')
        json_obj = json.loads(json_str)
        event = self.converter_mediator.dict_to_event(json_obj)
        self.message_bus.handle(event)

    def consume(self):
        if not self.channel:
            self.connect()
        self.channel.basic_consume(queue=self.queue, on_message_callback=self.call_back, auto_ack=True)
        self.channel.start_consuming()
