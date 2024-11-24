from dataclasses import dataclass
from src.domain.entities.report import Report
from src.domain.value_objects.script_action import ScriptAction
from src.domain.value_objects.video import Video
from src.domain.events.base import BaseEvent
from src.domain.entities.request import Request


@dataclass
class ArrivedNewRequest(BaseEvent):
    request: Request


@dataclass
class UploadedVideo(BaseEvent):
    video: Video


@dataclass
class SpeechRecognized(BaseEvent):
    video: Video


@dataclass
class ChekedScriptAction(BaseEvent):
    script_action: ScriptAction


@dataclass
class ComplitedReport(BaseEvent):
    request: Request
    report: Report