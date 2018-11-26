# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer
from task_queue import TaskQueue
from django.core.cache import cache


@api_view(['GET', 'POST'])
def get_post_employees(request):
    """
    get:
    Return a list of all the existing Employees.

    post:
    Create a new Employee.
    """
    if request.method == 'GET':
        if cache.get('employees'):
            return Response(cache.get('employees'))
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        cache.set('employees', serializer.data, 30) # 30 seconds
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # persist address
            zip_code_queue = TaskQueue()
            zip_code_queue.send_message(
                json.dumps({
                    "id_funcionario": serializer.data['id'],
                    "zip_code": serializer.data['zip_code']
                })
            )
            zip_code_queue.close_connection()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PATCH'])
def get_delete_patch_employee(request, id):
    """
    get:
    Return one existing Employee.

    patch:
    Update one Employee.

    delete:
    Delete an Employee.
    """
    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist:    
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    if request.method == 'PATCH':
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

