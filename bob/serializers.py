# -*- coding: utf-8 -*-
from rest_framework.serializers import ModelSerializer
from .models import Address


class AddressSerialiazer(ModelSerializer):

    class Meta:
        model = Address
