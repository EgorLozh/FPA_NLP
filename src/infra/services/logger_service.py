import logging
import sys

class LoggerService:
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        if not self.logger.handlers:
            self.logger.addHandler(handler)

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(LoggerService, cls).__new__(cls)
        return cls.instance

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)
    
    def warning(self, message):
        self.logger.warning(message)
