import pathlib

from infra.services.logger_service import LoggerService


class Speech2TextService:
    def __init__(self):
        model_dir = pathlib.Path().resolve().parent().parent()/"models"
        self.logger = LoggerService()