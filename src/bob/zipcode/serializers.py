from zipcode.models import ZipCode
from rest_framework import serializers


class ZipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZipCode
        fields = ('number', 'street', 'city', 'state')
