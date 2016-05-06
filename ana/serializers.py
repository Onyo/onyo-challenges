# -*- coding: utf-8 -*-
from rest_framework.serializers import ModelSerializer
from .models import Record


class RecordSerializer(ModelSerializer):

    class Meta:
        model = Record
        read_only_fields = ('address',)