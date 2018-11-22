# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer


@api_view(['GET', 'POST'])
def get_post_employees(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PATCH'])
def get_delete_patch_employee(request, id):
    try:
        employees = Employee.objects.get(id=id)
    except Employee.DoesNotExist:    
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = EmployeeSerializer(employees)
    return Response(serializer.data)
