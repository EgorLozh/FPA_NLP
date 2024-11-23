from src.infra.broker.converter.converter import EventConverterMediator


def init_event_converter() -> EventConverterMediator:
    event_converter_mediator = EventConverterMediator()

    # event_converter_mediator.register_event_to_dict_strategy()
    # event_converter_mediator.register_dict_to_event_strategy()

    return event_converter_mediator

init_event_converter()
