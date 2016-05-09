# -*- encoding: utf-8 -*-

from cep.models import Cep
from cep.serializers import CepSerializer
from django.shortcuts import render
from rest_framework import viewsets

class CepViewSet(viewsets.ModelViewSet):
    queryset = Cep.objects.all()
    serializer_class = CepSerializer
