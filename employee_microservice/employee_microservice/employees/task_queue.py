import pika
import sys

class TaskQueue:

    def __init__(self, task_queue_name):
        self.task_queue_name = task_queue_name
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=task_queue_name, durable=True)


    def send_message(self, message):
        self.channel.basic_publish(
            exchange='',
            routing_key=self.task_queue_name,
            body=message,
            properties=pika.BasicProperties(
                delivery_mode = 2, # make message persistent
            )
        )
        return "Sent"
    

    def close_connection(self):
        self.connection.close()