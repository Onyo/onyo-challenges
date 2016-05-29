from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Tickets
from .serializers import TicketsSerializer, UserTicketsSerializer


class TicketsView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Tickets.objects.all()
    serializer_class = TicketsSerializer


class TicketsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Tickets.objects.all()
    lookup_field = 'extraction'
    serializer_class = TicketsSerializer


class VerifyTicketsView(APIView):

    def post(self, request, extraction, format=None):
        """ Verify if a ticket is winner.

        Retrieve an extraction and a ticket and verify if is a winner ticket.
        ---
        serializer: TicketsSerializer
        omit_serializer: false

        responseMessages:
            - code: 404
              message: Extraction Not Found
            - code: 400
              message: Invalid parameters
        """
        try:
            winner_ticket = Tickets.objects.get(extraction=extraction)
            ticket = UserTicketsSerializer(data=request.data)
            if ticket.is_valid():
                is_winner = ticket.data['number'] == winner_ticket.number
                return Response(status=status.HTTP_200_OK, data={
                    'is_winner': is_winner,
                    **ticket.data
                })
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data=ticket.errors)
        except Tickets.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
