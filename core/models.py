from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import JSONField


class LottoTicket(models.Model):

    is_winner = models.BooleanField()
    numbers = JSONField()

    class Meta:
        abstract = True
