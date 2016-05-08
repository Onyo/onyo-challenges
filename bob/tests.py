import random

from django.test import TestCase
from django.test import Client

from bob.models import Address

from rest_framework import status


class AddressModelTest(TestCase):
    """
        Address Model Test
            Test CRUD
    """
    def setUp(self):
        data = {
            'post_code': ''.join([str(random.randint(0, 9)) for _ in range(8)]),
            'locality': 'Rua A',
            'street_number': 200,
            'country': 'BR',
            'state': 'PE',
            'city': 'Recife'            
        }
        self.address = Address.objects.create(**data)

    def tearDown(self):
        """   Test Address Delete   """
        self.address.delete()

    def test_address_create(self):
        """   Test Address Create   """
        address = self.address

        self.assertIsNotNone(address)
        self.assertTrue(isinstance(address, Address))

    def test_address_read(self):
        """   Test Address Read   """
        address = self.address

        self.assertEquals(address.__str__(), address.post_code)

    def test_address_update(self):
        """   Test Address Update   """
        address = self.address
        address.locality = "New Locality"
        address.save()

        self.assertEquals(address.locality, "New Locality")


class AddressClientTest(TestCase):
    """
        Address Client
            Testing HTTP Request
    """
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        data = {
            'post_code': ''.join([str(random.randint(0, 9)) for _ in range(8)]),
            'locality': 'Rua A',
            'street_number': 200,
            'country': 'BR',
            'state': 'PE',
            'city': 'Recife'
        }
        self.address = Address.objects.create(**data)

    def tearDown(self):
        self.address.delete()

    def test_get_address(self):
        """   Test GET Address   """
        response = self.client.get("/addresses/",
                                   content_type="application/json")
        self.failUnlessEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.json()[0]['post_code'])

    def test_post_address(self):
        """ Test POST Address """
        data = {
            'post_code': ''.join([str(random.randint(0, 9)) for _ in range(8)]),
            'locality': 'Rua B',
            'street_number': 300,
            'country': 'EUA',
            'state': '',
            'city': 'New York'
        }
        response = self.client.post("/addresses/", data)
        self.failUnlessEqual(response.status_code, status.HTTP_201_CREATED)
