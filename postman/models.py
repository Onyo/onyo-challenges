from django.db import models

class Location(models.Model):
    postcode = models.CharField(max_length=7)
    address = models.CharField(max_length=500)


