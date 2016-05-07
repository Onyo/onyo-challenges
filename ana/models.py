from django.db import models

from django.utils.translation import ugettext_lazy as _


class Record(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    post_code = models.CharField(max_length=8)
    address = models.CharField(max_length=530)

    class Meta:
        verbose_name_plural = _('Records')

    def __str__(self):
        return self.name
