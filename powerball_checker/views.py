from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from powerball_checker.serializers import TicketSerializer
from powerball_checker.models import Ticket
from rest_framework import mixins
from rest_framework import generics


class VerifyTicketView(APIView):

    """
    Check if a ticket is the winner of the prize
    """

    def post(self, request):
        ticket = TicketSerializer(
            data=request.data
        )

        if ticket.is_valid():
            return Response({'winner': ticket.winner()})

        return Response(
            ticket.errors, status=status.HTTP_400_BAD_REQUEST
        )


class CreateTicketView(mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
