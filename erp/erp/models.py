from django.core import validators
from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=20, unique=True)
    cep = models.CharField(
        max_length=10,
        validators=[
            validators.RegexValidator(r'^(\d\d\.\d\d\d-\d\d\d|\d\d\d\d\d-\d\d\d|\d\d\d\d\d\d\d\d)$'),
            validators.MinLengthValidator(8),
            validators.MaxLengthValidator(10),
        ],
    )
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    public_place = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % self.name
