from cliente.models import Cliente
from rest_framework import serializers


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'nome', 'cep', 'rua', 'cidade', 'estado')
        read_only_fields = ('id', 'rua', 'cidade', 'estado')
