from django.db import models
from datetime import date
from jsonfield import JSONField


class Prize(models.Model):
    draw_date = models.DateField(default=date.today)
    code = models.CharField(max_length=100)


class Ticket(models.Model):
    prize = models.ForeignKey(Prize)
    numbers = JSONField()
    winning = models.NullBooleanField()
    code = models.CharField(max_length=100)
