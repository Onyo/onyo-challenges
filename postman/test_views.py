from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Location

class LocationApiTests(APITestCase):
    fixtures = ['locations.json']

    def test_create_location(self):
        #number of locations before post
        locations_count_before_post = Location.objects.count()
        postcode = "22753340"

        url = reverse('locations')
        data = {"address": "Rua o tempo e o vento", "postcode": postcode}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Location.objects.count(), locations_count_before_post + 1)
        self.assertEqual(response.data['postcode'], postcode)

    def test_get_location(self):
        url = reverse('location-detail', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_location(self):
        new_postcode = "21051481"
        data = {"address": "Rua Dr. Tavares de Macedo", "postcode": new_postcode}
        url = reverse('location-detail', args=[2])
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['postcode'], new_postcode)
