from __future__ import absolute_import
import os
from celery import Celery
from celery import task
from celery import bootsteps
from kombu import Consumer, Exchange, Queue


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'address_microservice.settings')


my_queue = Queue('zip_code', Exchange('task_zip_codes'), 'zip_code')


app = Celery(broker='amqp://guest:guest@localhost:5672/')
app.autodiscover_tasks()

class MyConsumerStep(bootsteps.ConsumerStep):

    def get_consumers(self, channel):
        return [Consumer(channel,
                         queues=[my_queue],
                         callbacks=[self.handle_message],
                         accept=['json'])]

    def handle_message(self, body, message):
        print('Received message: {0!r}'.format(body))
        print(body)
        #call task
        app.tasks['addresses.tasks.check_address'].delay(body)
        message.ack()

app.steps['consumer'].add(MyConsumerStep)