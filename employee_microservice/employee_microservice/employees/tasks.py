from __future__ import absolute_import, unicode_literals
from celery import task
from .models import Employee
from .serializers import EmployeeSerializer
from django.core.exceptions import ObjectDoesNotExist
import json


@task(bind=True, name='employees.tasks.persist_address')
def persist_address(self, msg):
    print(msg)
    employee = Employee.objects.get(id=msg['id_funcionario'])
    serializer = EmployeeSerializer(employee, data={"address": msg['address']}, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('saved')
    else:
        print('invalid')