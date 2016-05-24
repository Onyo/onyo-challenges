from datetime import date

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Tickets


class TestTicketsView(APITestCase):

    def test_empty_field(self):
        """Ensure all fields are filled."""
        data = {}
        response = self.client.post('/tickets/', data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(response.data['extraction'],
                          ['This field is required.'])
        self.assertEqual(response.data['number'], ['This field is required.'])
        self.assertEquals(response.data['ruffle_date'],
                          ['This field is required.'])

    def test_extraction_higher_than_0(self):
        """Extraction should have value higher than 0"""
        data = {'extraction': 0}
        response = self.client.post('/tickets/', data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(response.data['extraction'],
                          ['Extraction must be higher then 1'])
        data['extraction'] = 1
        response = self.client.post('/tickets/', data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('extraction', response.data)

    def test_number_between_zero_and_999999(self):
        """Number should have value between 0 and 999999, both included."""
        data = {'number': -1}
        response = self.client.post('/tickets/', data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(response.data['number'],
                          ['Number must be between 0 and 999999'])
        data = {'number': 1000000}
        response = self.client.post('/tickets/', data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(response.data['number'],
                          ['Number must be between 0 and 999999'])
        data['number'] = 42
        response = self.client.post('/tickets/', data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('number', response.data)

    def test_ruffle_not_happened_yet(self):
        """Ruffle date should be higher or equal today"""
        data = {'ruffle_date': '1977-05-04'}
        response = self.client.post('/tickets/', data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(response.data['ruffle_date'],
                          ['Ruffle already happened.'])

    def test_create_ticket(self):
        """When all paremeters are correct a ticket should be raised."""
        data = {'extraction': 1, 'number': 1,
                'ruffle_date': date.today().strftime('%Y-%m-%d')}
        response = self.client.post('/tickets/', data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(Tickets.objects.count(), 1)

    def test_empty_list_ticket(self):
        """On a GET request, a ticket list is returned even if empty."""
        response = self.client.get('/tickets/')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data, [])

    def test_get_list_not_empty(self):
        """On a GET request, a ticket list is returned."""
        ticket = Tickets(**{'extraction': 1, 'number': 1,
                            'ruffle_date': date.today().strftime('%Y-%m-%d')})
        ticket.save()
        self.assertEquals(Tickets.objects.count(), 1)


class TicketsDetailView(APITestCase):
    pass  # Only authenticated


class VerifyTicketView(APITestCase):
    pass
