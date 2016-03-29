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
        url = reverse('location-detail', args=[21050530])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_location(self):
        new_postcode = "21051481"
        data = {"address": "Rua Dr. Tavares de Macedo", "postcode": new_postcode}
        url = reverse('location-detail', args=[21051480])
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['postcode'], new_postcode)

    def test_delete_location(self):
        locations_count_before_delete = Location.objects.count()
        url = reverse('location-detail', args=[21050530])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Location.objects.count(), locations_count_before_delete - 1)

    def test_get_locations(self):
        url = reverse('locations')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Location.objects.count())

    def test_get_new_location(self):
        locations_count_before_post = Location.objects.count()
        url = reverse('location-detail', args=[21540330])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Location.objects.count(), locations_count_before_post + 1)