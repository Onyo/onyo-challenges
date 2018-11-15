from rest_framework import serializers

from cep.models import Cep, City, State


class StateSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = State
        fields = ('name', 'acronym', 'url')


class CitySerializer(serializers.HyperlinkedModelSerializer):
    state = serializers.HyperlinkedRelatedField(queryset=State.objects.all(), view_name='state-detail')

    class Meta:
        model = City
        fields = ('name', 'state', 'url')


class CepSerializer(serializers.HyperlinkedModelSerializer):
    city = serializers.HyperlinkedRelatedField(queryset=City.objects.all(), view_name='city-detail')

    class Meta:
        model = Cep
        fields = ('cep', 'public_place', 'neighborhood', 'city', 'url')