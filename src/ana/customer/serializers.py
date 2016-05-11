from customer.models import Customer
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'zipcode', 'street', 'city', 'state')
        read_only_fields = ('id', 'street', 'city', 'state')
