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


class City(models.Model):
    name = models.CharField(max_length=200)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('name', 'state'))

    def __str__(self):
        return '%s(%s)' % (self.name, self.state.acronym)


class Cep(models.Model):
    cep = models.CharField(
        primary_key=True,
        # FIXME: hack - the DRF are using it to validate the input
        max_length=10,
        validators=[
            validators.RegexValidator(r'^(\d\d\.\d\d\d-\d\d\d|\d\d\d\d\d-\d\d\d|\d\d\d\d\d\d\d\d)$'),
            validators.MinLengthValidator(8),
            validators.MaxLengthValidator(10),
        ],
    )
    public_place = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)

    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.cep = ''.join(c for c in self.cep if c.isnumeric())
        super().save(*args, **kwargs)

    def __str__(self):
        return '%s' % self.cep
