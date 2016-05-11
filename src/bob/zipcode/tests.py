from django.test import TestCase
from zipcode.models import ZipCode

class ZipCodeTestCase(TestCase):

    def setUp(self):
        pass

    def test_save(self):
        zipcode = ZipCode()
        zipcode.number = 5533
        zipcode.street = "street 1"
        zipcode.city = "city example"
        zipcode.state = "state example"

        zipcode.save()
        self.assertEqual(zipcode.id, 1)
