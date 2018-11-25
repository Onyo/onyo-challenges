from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import Address
from .task_queue_pub import TaskQueuePub
from django.core.exceptions import ObjectDoesNotExist
import json


@shared_task(bind=True)
def check_address(self, msg):
    if msg['zip_code']:
        address = None
        try:
            address = Address.objects.get(zip_code=msg['zip_code'])
        except ObjectDoesNotExist:
            print('Error')
        
        if address:
            task = TaskQueuePub('task_addresses', 'address')
            message = {'funcionario_id': msg['funcionario_id'], 'address': address.address}
            task.send_message(json.dumps(message))