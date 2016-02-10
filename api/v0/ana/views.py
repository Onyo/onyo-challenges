# -*- coding: utf-8 -*-

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.v0.ana.exceptions import BobTicketBadRequestException
from api.v0.ana.serializers import LottoTicketSerializer
from api.v0.ana.repositories import LottoTicketRepository


class LottoTicketResultAPIView(APIView):

    def post(self, request, format='json'):
        serializer_class = LottoTicketSerializer
        request_serializer = serializer_class(data=request.data)

        if request_serializer.is_valid():
            repository = LottoTicketRepository()

            try:
                ticket = repository.get_by_numbers(request.data['numbers'])
            except BobTicketBadRequestException:
                return Response({'reason': 'Retrieving data from bob has failed.'}, status=status.HTTP_400_BAD_REQUEST)

            ticket_data = {
                'id': ticket.id,
                'numbers': ticket.numbers,
                'is_winner': ticket.is_winner,
            }
            return Response(ticket_data, status=status.HTTP_200_OK)
        else:
            return Response(request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
