from dotenv import load_dotenv
import pika
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(dotenv_path="{}/.env".format(current_dir))

credentials = pika.PlainCredentials(
    username=os.getenv('RABBITMQ_USER'),
    password=os.getenv('RABBITMQ_PASS'))

parameters = pika.ConnectionParameters(
    host=os.getenv('RABBITMQ_HOST'),
    credentials=credentials)

connection = pika.BlockingConnection(parameters=parameters)
channel = connection.channel()

channel.queue_declare(queue='stop')

channel.basic_publish(
    exchange='',
    routing_key='stop',
    body='')

connection.close()
