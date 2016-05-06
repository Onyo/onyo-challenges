from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

import requests
from requests import HTTPError


class Record(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    post_code = models.CharField(max_length=8)
    address = models.CharField(max_length=530)

    class Meta:
        verbose_name_plural = _('Records')


@receiver(post_save, sender=Record)
def get_address(sender, instance, **kwargs):
    if kwargs['created']:
        url = '%s/%s/' % (settings.BOB_URL, instance.post_code)
        try:
            response = requests.get(url)

            result = response.json()
            instance.address = ' - '.join(
                (result['post_code'], result['locality'], result['street_number'],
                 result['country'], result['state'], result['city'])
            )
            instance.save()
        except HTTPError:
            instance.name = None
            instance.email = None
            instance.post_code = None
            instance.address = None
