import pika
import sys

class TaskQueue:

    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='topic_zip_codes', exchange_type='topic', durable=True)


    def send_message(self, message):
        self.channel.basic_publish(
            exchange='topic_zip_codes',
            routing_key='zip_code',
            body=message,
            properties=pika.BasicProperties(
                headers={'tasks.add': {'exchange': 'topic_zip_codes', 'routing_key': 'zip_code'}},
                content_type="application/json",
                content_encoding='UTF-8',
                delivery_mode=2,
                priority=0,
            )
        )
        return "Sent"
    

    def close_connection(self):
        self.connection.close()