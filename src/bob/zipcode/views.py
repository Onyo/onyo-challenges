# -*- encoding: utf-8 -*-

from zipcode.models import ZipCode
from zipcode.serializers import ZipSerializer
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters

class ZipViewSet(viewsets.ModelViewSet):
    queryset = ZipCode.objects.all()
    serializer_class = ZipSerializer

    filter_backends = (filters.DjangoFilterBackend,)

    filter_fields = ('number',)
