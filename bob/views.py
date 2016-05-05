from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from .models import Address
from .serializers import AddressSerialiazer


class Addresses(APIView):

    def post(self, request):
        """
        Post method
        :param request:
        :return:
        """
        serializer = AddressSerialiazer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self):
        """
        Get method
        :return:
        """
        addresses = Address.objects.all()
        serializer = AddressSerialiazer(addresses)
        return Response(serializer.data)


def get_object(func):
    def func_wrapper(self, request, postcode):
        try:
            address = Address.objects.get(post_code=postcode)
        except Address.DoesNotExist:
            raise Http404
        return func(self, request, postcode, address)
    return func_wrapper


class AddressDetail(APIView):

    @get_object
    def get(self, request, postcode, address):
        """
        Get detail method
        :param request:
        :param postcode:
        :param address:
        :return:
        """
        serializer = AddressSerialiazer(address)
        return Response(serializer.data)
