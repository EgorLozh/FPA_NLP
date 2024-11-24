import pika



class BaseBrokerClient:
    def __init__(self, host: str, port: int, queue: str, user: str, password: str) -> None:
        self.host = host
        self.port = port
        self.queue = queue
        self.user = user
        self.password = password

        self.channel = None
        self.credentials = pika.PlainCredentials(self.user, self.password)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=self.host,
            port=self.port,
            credentials=self.credentials
        ))

    def connect(self):
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue)

    def close(self):
        if self.connection:
            self.connection.close()
    