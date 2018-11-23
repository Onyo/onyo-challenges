from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'name', 'zip_code', 'address', 'created_at', 'updated_at')