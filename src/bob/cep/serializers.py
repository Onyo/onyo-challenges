from cep.models import Cep
from rest_framework import serializers


class CepSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cep
        fields = ('cep', 'rua', 'cidade', 'estado')
