from django.db import models

class Location(models.Model):
    postcode = models.CharField(max_length=8, unique=True)
    address = models.CharField(max_length=500)