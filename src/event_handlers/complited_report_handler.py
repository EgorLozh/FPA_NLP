from configs import Settings
from src.infra.broker.publisher import Publisher
from src.infra.services.logger_service import LoggerService
from src.domain.events.base import BaseEventHandler
from src.domain.events.events import ComplitedReport
from src.infra.message_bus import MessageBus


class ComplitedReportHandler(BaseEventHandler):
    def __init__(self) -> None:
        settins = Settings()
        self.message_bus = MessageBus()
        self.logger = LoggerService()
        self.publisher = Publisher(
            host=settins.REBBIT_HOST,
            port=settins.AMQP_PORT,
            queue=settins.REBBIT_PUBLISH_QUEUE,
            user=settins.REBBIT_USER,
            password=settins.REBBIT_PASSWORD
        )

    def __call__(self, event: ComplitedReport) -> None:
        self.logger.info(f"Complited report")
        self.publisher.publish(event)