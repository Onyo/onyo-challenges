from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from powerball_checker.serializers import TicketSerializer


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
