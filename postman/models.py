# -*- coding: utf-8 -*-

from django.db import models
import random

ADDRESSES_TYPES = ['Avenida', 'Rua', 'Estrada']
ADDRESSES_PREFIXES = ['Doutor', 'Presidente', 'Senador']
ADDRESSES_FIRST_NAMES = ['João', 'Maria', 'Evandro', 'Gilberto', 'Sonia', 'Angela', 'Elisabeth', 'Antonio', 'Waldir']
ADDRESSES_LAST_NAMES = ['Pires', 'Souza', 'Lima', 'Silva', 'Vargas', 'Santos', 'Senna', 'Leite', 'Sonho']


class Location(models.Model):
    postcode = models.CharField(max_length=8, unique=True)
    address = models.CharField(max_length=500)

    @staticmethod
    def generate_address_name():
    	type_index = random.randint(0, len(ADDRESSES_TYPES) -1)
    	prefix_index = random.randint(0, len(ADDRESSES_PREFIXES) -1)
    	first_index = random.randint(0, len(ADDRESSES_FIRST_NAMES) -1)
    	last_index = random.randint(0, len(ADDRESSES_LAST_NAMES) -1)

    	return "%s %s %s %s" % (ADDRESSES_TYPES[type_index], ADDRESSES_PREFIXES[prefix_index], ADDRESSES_FIRST_NAMES[first_index], ADDRESSES_LAST_NAMES[last_index])
