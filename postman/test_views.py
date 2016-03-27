from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Location

class LocationApiTests(APITestCase):
    def test_create_location(self):
        #number of locations before post
        locations_count_before_post = Location.objects.count()

        url = reverse('locations')
        data = {"address": "Rua o tempo e o vento", "postcode": "22753340"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Location.objects.count(), locations_count_before_post + 1)