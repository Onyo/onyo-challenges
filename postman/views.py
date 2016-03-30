from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render_to_response
from django.http import Http404
from .models import Location
from .serializers import LocationSerializer

def index(request):
    locations = Location.objects.all()
    return render_to_response('locations-index.html', {"locations": locations, 'server_url': request.get_host()
})


class Locations(APIView):
    def get(self, request, format=None):
        """
        Retrieve all locations
        ---
        serializer: LocationSerializer
        """

        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Create a new location
        ---
        serializer: LocationSerializer
        """        
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LocationDetail(APIView):
    def get_object(self, postcode, create=False):
        try:
            return Location.objects.get(postcode=postcode)
        except Location.DoesNotExist:
            if create:
                #generate a random address name
                return Location.objects.create(address=Location.generate_address_name(), postcode=postcode)
            raise Http404

    def get(self, request, postcode, format=None):
        """
        Retrieve a location, if not found, create a new one with random address
        ---
        serializer: LocationSerializer
        """        
        location = self.get_object(postcode, True)
        serializer = LocationSerializer(location)
        return Response(serializer.data)

    def put(self, request, postcode, format=None):
        """
        Update a location, raise a Http404 exception when not found
        ---
        serializer: LocationSerializer
        """        
        location = self.get_object(postcode)
        serializer = LocationSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, postcode, format=None):
        """
        Delete a location, raise a Http404 exception when not found
        ---
        serializer: LocationSerializer
        """        

        location = self.get_object(postcode)
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)