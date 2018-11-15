from unittest import skip

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITransactionTestCase

from cep.models import State


class StateViewTests(APITransactionTestCase):

    def setUp(self):
        self.number_of_staties_before = State.objects.count()

    # FIXME:
    @skip('For a unknown reason the migration 0002 are not loaded')
    def test_list_predefined_state(self):
        url = reverse('state-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 27)

    def test_create_state(self):
        url = reverse('state-list')
        response = self.client.post(url, {'name': 'A new state', 'acronym': 'NS'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(State.objects.count(), self.number_of_staties_before + 1)

    def test_can_not_create_state_with_acronym_where_length_smaller_than_2(self):
        url = reverse('state-list')
        response = self.client.post(url, {'name': 'São Paulo', 'acronym': 'P'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(State.objects.count(), self.number_of_staties_before)

    def test_can_not_create_state_with_acronym_where_length_bigger_than_2(self):
        url = reverse('state-list')
        response = self.client.post(url, {'name': 'São Paulo', 'acronym': 'SSP'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(State.objects.count(), self.number_of_staties_before)

    def test_can_not_create_state_with_lower_case_acronym(self):
        url = reverse('state-list')
        response = self.client.post(url, {'name': 'São Paulo', 'acronym': 'sp'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(State.objects.count(), self.number_of_staties_before)

    def test_can_not_create_two_state_with_the_same_acronym(self):
        url = reverse('state-list')
        new_state = lambda: self.client.post(url, {'name': 'New State', 'acronym': 'NS'}, format='json')
        response = new_state()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(State.objects.count(), self.number_of_staties_before + 1)
        response = new_state()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(State.objects.count(), self.number_of_staties_before + 1)
