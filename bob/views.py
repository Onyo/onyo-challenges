from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.shortcuts import render_to_response

from .models import Address
from .serializers import AddressSerialiazer


def index(request):
    addresses = Address.objects.all()
    return render_to_response('index.html', {'addresses': addresses, 'url': request.get_host()})


class Addresses(APIView):

    def post(self, request, format=None):
        serializer = AddressSerialiazer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        addresses = Address.objects.all()
        serializer = AddressSerialiazer(addresses, many=True)
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
    def get(self, request, postcode, address, format=None):
        serializer = AddressSerialiazer(address)
        return Response(serializer.data)

    @get_object
    def put(self, request, postcode, address, format=None):
        serializer = AddressSerialiazer(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @get_object
    def delete(self, request, postcode, address, format=None):
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
