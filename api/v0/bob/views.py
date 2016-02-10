# -*- coding: utf-8 -*-
import random

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.v0.bob.models import LottoTicket
from api.v0.bob.serializers import LottoTicketSerializer


class LottoTicketResultAPIView(APIView):

    def post(self, request, format='json'):

        serializer = LottoTicketSerializer(data=request.data)

        if serializer.is_valid():

            try:
                ticket = LottoTicket.objects.get(numbers=request.data['numbers'])
                ticket_data = {
                    'id': ticket.id,
                    'numbers': ticket.numbers,
                    'is_winner': ticket.is_winner,
                }
            except LottoTicket.DoesNotExist:
                serializer.save(is_winner=bool(random.getrandbits(1)))
                ticket_data = serializer.data

            return Response(ticket_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
