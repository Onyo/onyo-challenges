from rest_framework import generics, permissions

from .models import Tickets
from .serializers import TicketsSerializer


class TicketsView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Tickets.objects.all()
    serializer_class = TicketsSerializer


class TicketsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Tickets.objects.all()
    lookup_field = 'extraction'
    serializer_class = TicketsSerializer
