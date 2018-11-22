import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Employee
from ..serializers import EmployeeSerializer

client = Client()

class GetEmployees(TestCase):

    def setUp(self):
        self.employee_1 = Employee.objects.create(name="Employee1", address="Davi street", zip_code="41320480")
        self.employee_2 = Employee.objects.create(name="Employee2", address="Main street", zip_code="41250240")


    def test_get_all_employees(self):
        ''' Test GET ALL Employees API '''
        response = client.get(reverse('get_all_employees'))
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_one_employee_valid(self):
        ''' Test GET ONE Employee BY ID API '''
        response = client.get(reverse('get_one_employee', kwargs={'id': self.employee_2.id}))
        employee = Employee.objects.get(id=self.employee_2.id)
        serializer = EmployeeSerializer(employee)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_one_employee_invalid(self):
        ''' Test GET ONE Employee BY ID INVALID API '''
        response = client.get(reverse('get_one_employee', kwargs={'id': 100}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)