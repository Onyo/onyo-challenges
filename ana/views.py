from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from .models import Record
from .serializers import RecordSerializer


class Records(APIView):
    def post(self, request, format=None):
        serializer = RecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        records = Record.objects.all()
        serializer = RecordSerializer(records, many=True)
        Response(serializer.data)


def get_object(func):
    def func_wrapper(self, request, postcode):
        try:
            record = Record.objects.get(post_code=postcode)
        except Record.DoesNotExist:
            raise Http404
        return func(self, request, postcode, record)
    return func_wrapper


class RecordDetail(APIView):

    @get_object
    def get(self, request, postcode, record, format=None):
        serializer = RecordSerializer(record)
        return Response(serializer.data)

    @get_object
    def put(self, request, postcode, record, format=None):
        serializer = RecordSerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @get_object
    def delete(self, request, postcode, record, format=None):
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
