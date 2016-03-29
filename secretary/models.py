from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
import requests

class Contact(models.Model):
    name = models.CharField(max_length=500)
    postcode = models.CharField(max_length=8)
    address = models.CharField(max_length=500)
    number = models.IntegerField(null=True, blank=True)

@receiver(post_save, sender=Contact)
def fill_address(sender, instance, **kwargs):    
    if kwargs['created']:
        #Get address information on postman
        response = requests.get(settings.POSTMAN_SERVICE_URL + str(instance.postcode))
        address_json = response.json()
        instance.address = address_json['address']
        instance.save() 
