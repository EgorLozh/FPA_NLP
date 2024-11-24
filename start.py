from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import pathlib

from configs import Settings

from src.infra.services.logger_service import LoggerService
from src.infra.broker.consumer import Consumer

from src.domain.events.events import ComplitedReport
from src.infra.broker.converter_mediator import ConverterMediator

from src.infra.broker.strategies.dict_to_event import RequestMessageToRequestEventStrategy
from src.infra.broker.strategies.event_to_dict import ComplitedReportToDictStrategy


def start():
    init_model()
    init_converter()
    
    settings = Settings()

    consumer = Consumer(
        host=settings.REBBIT_HOST,
        port=settings.AMQP_PORT,
        queue=settings.REBBIT_CONSUME_QUEUE,
        user=settings.REBBIT_USER,
        password=settings.REBBIT_PASSWORD
    )
    consumer.consume()


def init_model():
    logger = LoggerService()

    logger.info("Initializing model...")
    try:
        model_dir = pathlib.Path().resolve() / "models"
        model_name = "Qwen/Qwen2.5-0.5B-Instruct"
        
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype="auto",
            device_map="auto",
            cache_dir=model_dir
        )

        if torch.cuda.is_available():
            model.to("cuda")
        
        logger.info(f"Model device: {model.device}")

    except Exception as e:
        logger.error(f"Error loading model: {str(e)}")
        raise e





def init_converter() -> ConverterMediator:
    converter_mediator = ConverterMediator()

    converter_mediator.register_dict_to_event_strategy('request', RequestMessageToRequestEventStrategy())
    converter_mediator.register_event_to_dict_strategy(ComplitedReport, ComplitedReportToDictStrategy())

    return converter_mediator


if __name__ == "__main__":
    start()