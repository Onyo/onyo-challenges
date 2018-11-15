from rest_framework import viewsets

from .models import State
from .serializers import StateSerializer


class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
