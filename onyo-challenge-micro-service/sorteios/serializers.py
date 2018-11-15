from rest_framework import serializers
from .models import Sorteio, Resultado


class SorteioSerializer(serializers.ModelSerializer):
    def validate(self, data):
        """
        Confere se a quantidade de Valores é um número entre minimo e maximo
        """
        if data['minimo'] > data['maximo']:
            raise serializers.ValidationError(
                {"minimo": "O valor mínimo do sorteio deve ser menor que o máximo"})

        if data['quantidadeValores'] > data['maximo'] - data['minimo']:
            raise serializers.ValidationError(
                {"quantidadeValores": "A quantidade de valores do sorteio não deve exceder a diferença entre o máximo e o mínimo"})
        return data

    class Meta:
        model = Sorteio
        fields = ('id', 'nome', 'quantidadeValores', 'minimo',
                  'maximo', 'owner', 'realizado', 'data_realizado')


class ResultadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resultado
        fields = ('id', 'sorteio', 'resultado', )
