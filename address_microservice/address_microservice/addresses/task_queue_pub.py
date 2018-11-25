import pika
import sys

class TaskQueuePub:

    def __init__(self, exchange, routing_key):
        self.exchange = exchange
        self.routing_key = routing_key
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=self.exchange, exchange_type='topic', durable=True)


    def send_message(self, message):
        self.channel.basic_publish(
            exchange=self.exchange,
            routing_key=self.routing_key,
            properties=pika.BasicProperties(
                headers={'tasks.add': {'exchange': self.exchange, 'routing_key': self.routing_key}},
                content_type="application/json",
                content_encoding='UTF-8',
                delivery_mode=2,
                priority=0,

            ),
            body=message
        )
        self.connection.close()
        return "Sent"
