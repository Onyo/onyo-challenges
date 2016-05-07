# -*- coding: utf-8 -*-
from django.conf import settings
from rest_framework.serializers import ModelSerializer, ValidationError
from rest_framework import status

from .models import Record

import requests
from requests import HTTPError


class RecordSerializer(ModelSerializer):

    class Meta:
        model = Record
        read_only_fields = ('address',)

    def create(self, validated_data):
        url = '%s/%s/' % (settings.BOB_URL, validated_data['post_code'])
        try:
            response = requests.get(url)
            if response.status_code == status.HTTP_200_OK:
                result = response.json()
                validated_data['address'] = ' - '.join(
                    (result['locality'], result['street_number'],
                     result['country'], result['state'], result['city'])
                )
            else:
                validated_data['address'] = None
        except HTTPError as error:
            raise error

        if not validated_data['address']:
            raise ValidationError('Postcode Not Found!')
        return Record.objects.create(**validated_data)