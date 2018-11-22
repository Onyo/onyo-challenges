import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Employee
from ..serializers import EmployeeSerializer

client = Client()

class GetAllEmployees(TestCase):

    def setUp(self):
        Employee.objects.create(name="Employee1", address="Davi street", zip_code="41320480")
        Employee.objects.create(name="Employee2", address="Main street", zip_code="41250240")
    
    def test_get_all_employees(self):
        response = client.get(reverse('get_all_employees'))
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)