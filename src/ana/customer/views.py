# -*- encoding: utf-8 -*-

from customer.models import Customer
from customer.serializers import CustomerSerializer
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework import filters
from rest_framework.response import Response
from ana.settings import BOB_API_URL 
import requests

class CustomerViewSet(viewsets.ModelViewSet):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id','zipcode','state')

    #Custom create method to call BOB Api and set other fields
    def create(self, request):
        
        serializer = CustomerSerializer(data=request.data)

        if serializer.is_valid():
            customer = Customer()
            customer.name = serializer['name'].value
            customer.zipcode = serializer['zipcode'].value

            #Call BOB Api
            r = requests.get(BOB_API_URL.format(customer.zipcode))
            if r.status_code == 200 and r.json()['results']:
                print("ZipCode found")
                ret = r.json()['results'][0]
                customer.street = ret['street']
                customer.state = ret['state']
                customer.city = ret['city']
            else:
                print("zipCode not found on BOB_API")


            self.perform_create(customer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
