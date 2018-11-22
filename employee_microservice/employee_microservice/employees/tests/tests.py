# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from ..models import Employee


class EmployeeTest(TestCase):

    def setUp(self):
        Employee.objects.create(name="Employee1", address="Davi street", zip_code="41320480")
    
    def test_get_all(self):
        all_employees = Employee.objects.all()
        self.assertEqual(all_employees.count(), 1)

    def test_get_one(self):
        one_employee = Employee.objects.get(id=1)
        self.assertEqual(one_employee.name, "Employee1")
