# -*- encoding: utf-8 -*-

from cep.models import Cep
from cep.serializers import CepSerializer
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters

class CepViewSet(viewsets.ModelViewSet):
    queryset = Cep.objects.all()
    serializer_class = CepSerializer

    filter_backends = (filters.DjangoFilterBackend,)

    filter_fields = ('cep',)
