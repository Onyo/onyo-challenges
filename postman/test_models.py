from django.test import TestCase
from postman.models import Location

class LocationTestCase(TestCase):
    def setUp(self):
        Location.objects.create(address="Rua o tempo e o vento", postcode="22753340")
        Location.objects.create(address="Rua Dr. Tavares de Macedo", postcode="21051480")

    def test_find_location_by_postcode(self):
        location = Location.objects.get(postcode="22753340")
        self.assertEqual(Location.objects.first().postcode, location.postcode)

    def test_delete_location_by_postcode(self):
        Location.objects.get(postcode="22753340").delete()
        with self.assertRaises(Location.DoesNotExist):
        	Location.objects.get(postcode="22753340")
        