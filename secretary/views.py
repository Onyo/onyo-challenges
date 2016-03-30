from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render_to_response
from django.http import Http404
from .models import Contact
from .serializers import ContactSerializer

def index(request):
    contacts = Contact.objects.all()
    return render_to_response('contacts-index.html', {"contacts": contacts, 'server_url': request.get_host()
})


class Contacts(APIView):
    def get(self, request, format=None):
        """
        Retrieve all contacts
        ---
        serializer: ContactSerializer
        """
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Create new contact, and fills the address using postman service searching by its postcode 
        ---
        serializer: ContactSerializer
        """
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
        """
        Retrieve a contact, raise a Http404 exception when not found
        ---
        serializer: ContactSerializer
        """
        contact = self.get_object(pk)
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        Update a contact, raise a Http404 exception when not found
        ---
        serializer: ContactSerializer
        """
        contact = self.get_object(pk)
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Delete a contact, raise a Http404 exception when not found
        ---
        serializer: ContactSerializer
        """
        contact = self.get_object(pk)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        