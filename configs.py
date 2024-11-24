from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    REBBIT_USER: str
    REBBIT_PASSWORD: str
    REBBIT_HOST: str
    REBBIT_PORT: int
    AMQP_PORT: int
    REBBIT_CONSUME_QUEUE: str
    REBBIT_PUBLISH_QUEUE: str

    class Config:
        env_file = ".env"
        extra = "allow"
