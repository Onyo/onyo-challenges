from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer


class Contacts(APIView):
    def get(self, request, format=None):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactDetail(APIView):
    def get_object(self, pk):
        try:
            return Contact.objects.get(pk=pk)
        except Contact.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        contact = self.get_object(pk)
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        contact = self.get_object(pk)
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        contact = self.get_object(pk)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        