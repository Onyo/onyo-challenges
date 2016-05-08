from django.db import models

from django.utils.translation import ugettext_lazy as _


class Address(models.Model):
    post_code = models.CharField(max_length=8, unique=True)
    locality = models.CharField(max_length=200)
    street_number = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=40, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True)

    class Meta:
        verbose_name_plural = _('Addresses')

    def __str__(self):
        return self.post_code
