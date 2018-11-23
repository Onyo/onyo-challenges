# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Address(models.Model):

    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
