from rest_framework import generics, permissions

from .models import Tickets
from .serializers import TicketsSerializer


class TicketsView(generics.ListCreateAPIView):
    queryset = Tickets.objects.all()
    serializer_class = TicketsSerializer


class TicketsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Tickets.objects.all()
    serializer_class = TicketsSerializer
