from rest_framework.response import Response
from rest_framework.views import APIView
from powerball_checker.serializers import TicketSerializer


class VerifyTicketView(APIView):

    """
    Check if a ticket is the winner of the prize
    """

    def post(self, request):
        t = TicketSerializer(
            data=request.data)

        if t.is_valid():
            return Response({'winner': t.winner()})
