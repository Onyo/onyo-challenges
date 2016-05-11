from django.db import models

class ZipCode(models.Model):
    number = models.BigIntegerField()
    street = models.CharField(max_length=1000)
    city = models.CharField(max_length=500)
    state = models.CharField(max_length=2)
