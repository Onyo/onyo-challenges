from unittest import skip

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITransactionTestCase

from cep.models import City


class CityViewTests(APITransactionTestCase):

    def setUp(self):
        self.number_of_cities_before = City.objects.count()

    # FIXME:
    @skip('For a unknown reason the migration 0002 are not loaded')
    def test_list_predefined_cities(self):
        url = reverse('city-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_cannot_repeat_city_name_on_same_state(self):
        fake_state_url = self.client.post(
            reverse('state-list'), {
                'name': 'fake city',
                'acronym': 'FC'
            }, format='json'
        ).data['url']

        url = reverse('city-list')
        create_city = lambda: self.client.post(url, {'name': 'Vitória da Conquista', 'state': fake_state_url}, format='json')

        response = create_city()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(City.objects.count(), self.number_of_cities_before + 1)
        response = create_city()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(City.objects.count(), self.number_of_cities_before + 1)
