from django.core import validators
from django.db import models


class State(models.Model):
    name = models.CharField(max_length=20, unique=True)
    acronym = models.CharField(
        unique=True,
        max_length=2,
        validators=[
            validators.MinLengthValidator(2),
            validators.RegexValidator(r'^[A-Z]{2}$', message='Ensure all letter be capitalized.')
        ]
    )

    def __str__(self):
        return '%s(%s)' % (self.name, self.acronym)
