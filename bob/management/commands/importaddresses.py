import csv
import os
import sys

from django.core.management import BaseCommand
from bob.models import Address


# The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):
    # Show this when the user types help
    help = "Import Addresses"

    def add_arguments(self, parser):
        parser.add_argument('file', type=lambda s: file_choices(s),
                            default=sys.stdin,
                            help='CSV file with addresses')

        def file_choices(fname):
            choices = ("csv",)
            ext = os.path.splitext(fname)[1][1:]
            if ext not in choices:
                parser.error("file doesn't end with one of {}".format(choices))
            return fname

    # A command must define handle()
    def handle(self, *args, **options):
        self.stdout.write('Starting importation...')
        with open(options['file'], 'r') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            for row in spamreader:
                self.stdout.write('Data: ' + row)
                data = {
                    'post_code': row[0],
                    'locality': row[1],
                    'street_number': row[2],
                    'country': row[3],
                    'state': row[4],
                    'city': row[5]
                }
                address, _ = Address.objects.get_or_create(**data)
        self.stdout.write('Done...')
