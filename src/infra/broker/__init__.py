from functools import lru_cache

from src.domain.events.events import ComplitedReport
from src.infra.broker.converter_mediator import ConverterMediator

from src.infra.broker.strategies.dict_to_event import RequestMessageToRequestEventStrategy
from src.infra.broker.strategies.event_to_dict import ComplitedReportToDictStrategy


@lru_cache(1)
def init_converter() -> ConverterMediator:
    converter_mediator = ConverterMediator()

    converter_mediator.register_dict_to_event_strategy('request', RequestMessageToRequestEventStrategy())
    converter_mediator.register_event_to_dict_strategy(ComplitedReport, ComplitedReportToDictStrategy())

    return converter_mediator

init_converter()
