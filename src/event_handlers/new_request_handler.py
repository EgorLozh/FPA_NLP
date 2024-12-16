import pathlib

from configs import Settings
from src.domain.entities.report import Report
from src.domain.value_objects.mark import Mark
from src.domain.events.base import BaseEventHandler
from src.domain.events.events import ArrivedNewRequest, ComplitedReport
from src.infra.message_bus import MessageBus
from src.infra.services.LLM_service import LLMService
from src.infra.services.logger_service import LoggerService
from src.infra.services.video_service import VideoService
from src.infra.services.speech2text_service import Speech2TextService


class NewRequestHandler(BaseEventHandler):
    def __init__(self):
        self.logger = LoggerService()
        self.llm_service = LLMService()
        self.video_service = VideoService()
        self.speech2text_service = Speech2TextService()
        self.message_bus = MessageBus()

    def delete_file(self, file_path):
        pathlib.Path.unlink(file_path, missing_ok=True)

    def __call__(self, event: ArrivedNewRequest) -> None:
        path = pathlib.Path().resolve()

        video = event.request.video
        video.file_name = str(path/"video.mp4")
        self.video_service.download_video(video.url, video.file_name)

        audio = str(path/"audio.wav")
        self.video_service.extarct_audio(video.file_name, audio)

        # TODO: change way of remooving noises now it is not working
        # self.speech2text_service.remove_noises(audio)
        speech = self.speech2text_service.recognize(audio)
        video.speech = speech

        self.delete_file(audio)
        self.delete_file(video.file_name)

        script = event.request.script
        marks = []
        report = Report(marks=marks, request=event.request)

        for i, action in enumerate(script.actions):
            self.logger.info(f"Processing action {i+1} from {len(script.actions)}...")

            action.script = script
            promt = f""" 
Сейчас будет диалог продавца с покупателем. Запомни его и ответь на вопрос. 
Сам диалог:
{speech}

Это был диалог продавца с покупателем. Теперь ответь на вопрос выполнил ли продавец следующее действие ?: "{action.text}"
Отвечай только "да" или "нет".
"""
            answer = self.llm_service.generate(promt).lower()
            mark = Mark(script_action=action, check='да' in answer, report=report)
            marks.append(mark)

            self.logger.info(f"Action {i+1} processed")

        self.logger.info("All actions processed")

        self.message_bus.handle(ComplitedReport(report=report, request=event.request))





