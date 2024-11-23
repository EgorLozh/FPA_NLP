from src.domain.events.base import BaseEvent
from src.infra.broker.base import BaseBrokerClient


class Publisher(BaseBrokerClient):

    def publish(self, event: BaseEvent):
        if not self.channel:
            self.connect()

        to_dict_strategy = self.mediator.get_event_to_dict_strategy(event.__class__)
        message = to_dict_strategy.event_to_dict(event)

        self.channel.basic_publish(exchange='', routing_key=self.queue, body=message)
    