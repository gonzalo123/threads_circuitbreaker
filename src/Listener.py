from queue import Queue, Empty
import threading
import pika
import os


class Listener(threading.Thread):
    def __init__(self, queue=Queue()):
        super(Listener, self).__init__()
        self.queue = queue
        self.daemon = True

    def run(self):
        channel = self._get_channel()
        channel.queue_declare(queue='stop')

        channel.basic_consume(
            queue='stop',
            on_message_callback=lambda ch, method, properties, body: self.queue.put(item=True),
            auto_ack=True)

        channel.start_consuming()

    def stop(self):
        try:
            return True if self.queue.get(timeout=0.05) is True else False
        except Empty:
            return False

    def _get_channel(self):
        credentials = pika.PlainCredentials(
            username=os.getenv('RABBITMQ_USER'),
            password=os.getenv('RABBITMQ_PASS'))

        parameters = pika.ConnectionParameters(
            host=os.getenv('RABBITMQ_HOST'),
            credentials=credentials)

        connection = pika.BlockingConnection(parameters=parameters)

        return connection.channel()
