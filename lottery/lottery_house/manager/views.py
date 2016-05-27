import requests
from django.conf import settings
from requests.exceptions import Timeout
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Tickets
from .serializers import TicketsSerializer


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
        omit_serializer: true

        responseMessages:
            - code: 404
              message: Extraction Not Found
            - code: 503
              message: Service Unavailble
            - code: 400
              message: Invalid parameters
        """
        serializer = TicketsSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            response = requests.post(
                'http://{host}/tickets/{extraction}/verify/'.format(
                    extraction=extraction,
                    host=settings.BOB_HOST,
                ),
                data=serializer.data,
                timeout=1
            )
        except Timeout:
            return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)
        if response.ok:
            return Response(data=response.json(),
                            status=status.HTTP_200_OK)
        elif response.status_code == status.HTTP_404_NOT_FOUND:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)
