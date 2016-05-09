# -*- encoding: utf-8 -*-

from cliente.models import Cliente
from cliente.serializers import ClienteSerializer
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework import filters
from rest_framework.response import Response
from ana.settings import BOB_API_URL 
import requests

class ClienteViewSet(viewsets.ModelViewSet):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id','cep','estado')

    #Custom create method to call BOB Api and set other fields
    def create(self, request):
        
        serializer = ClienteSerializer(data=request.data)

        if serializer.is_valid():
            cliente = Cliente()
            cliente.nome = serializer['nome'].value
            cliente.cep = serializer['cep'].value

            #Call BOB Api
            r = requests.get(BOB_API_URL.format(cliente.cep))
            if r.status_code == 200 and r.json()['results']:
                print("CEP found")
                ret = r.json()['results'][0]
                cliente.rua = ret['rua']
                cliente.estado = ret['estado']
                cliente.cidade = ret['cidade']
            else:
                print("CEP not found on BOB_API")


            self.perform_create(cliente)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
