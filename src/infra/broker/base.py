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
            credentials=self.credentials,
            heartbeat=600
        ))

    def connect(self):
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue)

    def close(self):
        if self.connection:
            self.connection.close()

    def reconnect(self):
        if self.connection and not self.connection.is_closed:
            self.connection.close()

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=self.host,
            port=self.port,
            credentials=self.credentials
        ))
        self.connect()
    