from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=500)
    postcode = models.CharField(max_length=8)
    address = models.CharField(max_length=500)
    number = models.IntegerField(null=True, blank=True)
