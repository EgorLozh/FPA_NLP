from src.domain.events.base import BaseEvent
from src.domain.entities.request import Request
from src.domain.entities.script import Script
from src.domain.value_objects.video import Video
from src.domain.value_objects.script_action import ScriptAction

from src.domain.events.events import ArrivedNewRequest
from src.infra.broker.strategies.base import BaseDictToEventStartegy
from src.infra.broker.schemas import RequestMessageSchema


class RequestMessageToRequestEventStrategy(BaseDictToEventStartegy):
    @staticmethod
    def dict_to_event(json) -> BaseEvent:
        request_message_schema = RequestMessageSchema.model_validate(json)

        video = Video(
            url=request_message_schema.data.video.url
        )

        script = Script()
        actions = [ScriptAction(text=action.text, weight=action.weight, script=script) 
                   for action in request_message_schema.data.actions]
        script.actions = actions

        request = Request(
            oid=request_message_schema.data.id,
            video=video,
            script=script
        )

        video.request = request
        script.request = request

        return ArrivedNewRequest(request)


