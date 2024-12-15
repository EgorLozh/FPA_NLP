import json
import pika

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
        try:
            if not self.channel or self.channel.is_closed:
                self.connect()

            self.channel.basic_consume(queue=self.queue, on_message_callback=self.call_back, auto_ack=True)
            self.channel.start_consuming()
        except pika.exceptions.ConnectionClosedByBroker:
            self.logger.error("Connection closed by broker, reconnecting...")
            self.reconnect()
            self.consume()
        except pika.exceptions.AMQPChannelError as err:
            self.logger.error(f"Channel error: {err}")
            self.reconnect()
        except pika.exceptions.AMQPConnectionError as err:
            self.logger.error(f"Connection error: {err}")
            self.reconnect()
