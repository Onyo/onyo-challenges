from rest_framework import serializers

from cep.models import State


class StateSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = State
        fields = ('name', 'acronym', 'url')
