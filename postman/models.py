# -*- coding: utf-8 -*-

from django.db import models
import random


class Location(models.Model):
    ADDRESSES_TYPES = ['Avenida', 'Rua', 'Estrada']
    ADDRESSES_PREFIXES = ['Doutor', 'Presidente', 'Senador', "Dom"]
    ADDRESSES_FIRST_NAMES = ['João', 'Maria', 'Evandro', 'Gilberto', 'Sonia', 'Angela', 'Elisabeth', 'Antonio', 'Waldir', "Helder"]
    ADDRESSES_LAST_NAMES = ['Pires', 'Souza', 'Lima', 'Silva', 'Vargas', 'Santos', 'Senna', 'Leite', 'Sonho', "Camara"]

    postcode = models.CharField(max_length=8, unique=True)
    address = models.CharField(max_length=500)

    @staticmethod
    def generate_address_name():
        type_index = random.randint(0, len(Location.ADDRESSES_TYPES) -1)
        prefix_index = random.randint(0, len(Location.ADDRESSES_PREFIXES) -1)
        first_index = random.randint(0, len(Location.ADDRESSES_FIRST_NAMES) -1)
        last_index = random.randint(0, len(Location.ADDRESSES_LAST_NAMES) -1)

        return "%s %s %s %s" % (Location.ADDRESSES_TYPES[type_index], 
            Location.ADDRESSES_PREFIXES[prefix_index], 
            Location.ADDRESSES_FIRST_NAMES[first_index], 
            Location.ADDRESSES_LAST_NAMES[last_index])
