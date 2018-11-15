from rest_framework import viewsets

from cep.models import State
from cep.serializers import StateSerializer


class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
