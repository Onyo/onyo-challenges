import requests
from requests.exceptions import Timeout

from django.conf import settings
from django.core.cache import cache
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Tickets
from .serializers import (TicketsSerializer, UserTicketsSerializer,
                          WinnerTicketsSerializer)


class TicketsView(generics.ListCreateAPIView):
    queryset = Tickets.objects.all()
    serializer_class = TicketsSerializer


class TicketsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Tickets.objects.all()
    serializer_class = TicketsSerializer


class VerifyTicketsView(APIView):

    def post(self, request, extraction, format=None):
        """ Verify if a ticket is winner.

        Retrieve an extraction and a ticket and verify if is a winner ticket.
        ---
        serializer: TicketsSerializer
        response_serializer: WinnerTicketsSerializer
        omit_serializer: false

        responseMessages:
            - code: 404
              message: Extraction Not Found
            - code: 503
              message: Service Unavailble
            - code: 400
              message: Invalid parameters
        """
        serializer = UserTicketsSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        cached = cache.get('E{extraction}N{number}'.format(**serializer.data))
        if cached:
            return Response(status=status.HTTP_200_OK, data=cached)
        try:
            response = requests.post(
                'http://{host}/tickets/{extraction}/verify'.format(
                    extraction=extraction,
                    host=settings.BOB_HOST,
                ),
                data=serializer.data,
                timeout=1
            )
        except Timeout:
            return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)
        if response.ok:
            response_ticket = WinnerTicketsSerializer(data=response.json())
            if response_ticket.is_valid():
                cache.set(('E{extraction}N{number}'.format(**serializer.data)),
                          response_ticket.data)
                return Response(data=response_ticket.data,
                                status=status.HTTP_200_OK)
        elif response.status_code == status.HTTP_404_NOT_FOUND:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)
