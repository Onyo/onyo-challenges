from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Location
from .serializers import LocationSerializer
from django.shortcuts import render_to_response


def index(request):
    locations = Location.objects.all()
    return render_to_response('location-index.html', {"locations": locations, 'server_url': request.get_host()
})


class Locations(APIView):
    def get(self, request, format=None):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LocationDetail(APIView):
    def get_object(self, postcode):
        try:
            return Location.objects.get(postcode=postcode)
        except Location.DoesNotExist:
            #generate a random address name
            return Location.objects.create(address=Location.generate_address_name(), postcode=postcode)

    def get(self, request, postcode, format=None):
        location = self.get_object(postcode)
        serializer = LocationSerializer(location)
        return Response(serializer.data)

    def put(self, request, postcode, format=None):
        location = self.get_object(postcode)
        serializer = LocationSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, postcode, format=None):
        location = self.get_object(postcode)
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)