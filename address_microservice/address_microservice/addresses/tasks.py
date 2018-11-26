from __future__ import absolute_import, unicode_literals
from celery import task
from .models import Address
from .task_queue_pub import TaskQueuePub
from django.core.exceptions import ObjectDoesNotExist
import json


@task(bind=True, name='addresses.tasks.check_address')
def check_address(self, msg):
    if msg['zip_code']:
        address = None
        try:
            address = Address.objects.get(zip_code=msg['zip_code'])
        except ObjectDoesNotExist:
            print('Error')
        
        if address:
            task = TaskQueuePub('topic_addresses', 'address')
            message = {'id_funcionario': msg['id_funcionario'], 'zip_code': msg['zip_code'], 'address': address.address}
            print(message)
            task.send_message(json.dumps(message))