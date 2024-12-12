from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    RABBIT_USER: str
    RABBIT_PASSWORD: str
    RABBIT_HOST: str
    RABBIT_PORT: int
    AMQP_PORT: int
    RABBIT_CONSUME_QUEUE: str
    RABBIT_PUBLISH_QUEUE: str

    LLM_MODEL_NAME: str
    VOSK_MODEL_NAME: str

    class Config:
        env_file = ".env"
        extra = "allow"
