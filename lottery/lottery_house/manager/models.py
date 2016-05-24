from django.db import models


class Tickets(models.Model):
    extraction = models.PositiveIntegerField()
    number = models.PositiveIntegerField()
    ruffle_date = models.DateField()

    def __str__(self):
        return 'Extraction: {} Ticket Number: {:06}'.format(self.extraction,
                                                            self.number)
