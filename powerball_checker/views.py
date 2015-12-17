from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from powerball_checker.serializers import TicketSerializer, PrizeSerializer
from powerball_checker.models import Ticket, Prize
from rest_framework import mixins
from rest_framework import generics


class ListPrizesView(ListAPIView):
    queryset = Prize.objects.all().order_by('draw_date')
    serializer_class = PrizeSerializer


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
