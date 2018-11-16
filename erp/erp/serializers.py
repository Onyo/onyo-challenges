from rest_framework import serializers

from erp.models import Employee
from erp.cep import get_address_from_cep


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Employee
        fields = ('name', 'cep', 'city', 'state', 'public_place', 'neighborhood', 'url')
        extra_kwargs = {
            'city': {
                'required': False
            },
            'state': {
                'required': False
            },
            'public_place': {
                'required': False
            },
            'neighborhood': {
                'required': False
            },
        }

    def validate(self, data):
        is_missing_data = not all(['city' in data, 'state' in data, 'public_place' in data, 'neighborhood' in data])
        if is_missing_data:
            address = get_address_from_cep(data['cep'])
            if address is None:
                raise serializers.ValidationError('Can not access the CEP service or cep is unknown, please add all address info')
            data['city'] = address.city.name
            data['state'] = address.city.state.name
            data['public_place'] = address.public_place
            data['neighborhood'] = address.neighborhood
        return data
