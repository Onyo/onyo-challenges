from django.db import models
from datetime import date
from jsonfield import JSONField


class Prize(models.Model):
    date = models.DateField(default=date.today)


class WinningNumbers(models.Model):
    prize = models.ForeignKeys(Prize)
    numbers = JSONField()
