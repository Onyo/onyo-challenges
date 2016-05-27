from datetime import date, timedelta
from unittest.mock import call, patch

from requests.exceptions import Timeout

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase

from .models import Tickets
from .views import VerifyTicketsView


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


class TestTicketsDetailView(APITestCase):

    def setUp(self):
        self.ticket = Tickets(**{
            'extraction': 1,
            'number': 1,
            'ruffle_date': date.today().strftime('%Y-%m-%d')
        })
        self.ticket.save()
        self.user = User.objects.create_user('John Cleese',
                                             'eric@cheeseshop.com',
                                             'johnpassword')
        self.user.save()

    def test_unauthenticated_partial_update(self):
        """Partial update is only allow when user is athenticated"""
        response = self.client.patch('/tickets/1')
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEquals(response.data['detail'], 'Authentication credentials'
                          ' were not provided.')

    def test_unauthenticated_complete_update(self):
        """Complete update is only allow when user is athenticated"""
        response = self.client.put('/tickets/1')
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEquals(response.data['detail'], 'Authentication credentials'
                          ' were not provided.')

    def test_unauthenticated_delete(self):
        """Delete is only allow when user is athenticated"""
        response = self.client.put('/tickets/1')
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEquals(response.data['detail'], 'Authentication credentials'
                          ' were not provided.')

    def test_retrieve_ticket(self):
        """Allow retrieve a ticket even if unauthenticated."""
        response = self.client.get('/tickets/1')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data['id'], 1)
        self.assertEquals(response.data['extraction'], 1)
        self.assertEquals(response.data['number'], 1)
        self.assertEquals(response.data['ruffle_date'],
                          date.today().strftime('%Y-%m-%d'))

    def test_partial_update_ticket(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.patch('/tickets/1', {'number': 2})
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data['id'], 1)
        self.assertEquals(response.data['extraction'], 1)
        self.assertEquals(response.data['number'], 2)
        self.assertEquals(response.data['ruffle_date'],
                          date.today().strftime('%Y-%m-%d'))

    def test_complete_update_ticket(self):
        tomorrow = (date.today() + timedelta(days=1)).strftime('%Y-%m-%d')
        self.client.force_authenticate(user=self.user)
        response = self.client.put('/tickets/1', {
            'number': 2,
            'extraction': 2,
            'ruffle_date': tomorrow})
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data['number'], 2)
        self.assertEquals(response.data['extraction'], 2)
        self.assertEquals(response.data['number'], 2)
        self.assertEquals(response.data['ruffle_date'], tomorrow)

    def test_delete_ticket(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete('/tickets/1')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(Tickets.objects.count(), 0)


class TestVerifyTicketsView(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.valid_ticket = {
            'extraction': 1,
            'number': 1,
            'ruffle_date': date.today().strftime('%Y-%m-%d')
        }

    @patch('manager.views.requests')
    def test_third_party_api_respond_500(self, mock_requests):
        mock_requests.post.return_value.status_code = 500
        mock_requests.post.return_value.ok = False
        request = self.factory.post('/tickets/1/verify',
                                    data=self.valid_ticket)
        response = VerifyTicketsView.as_view()(request, 1)
        self.assertEqual(response.status_code, 503)
        self.assertTrue(mock_requests.post.called)

    @patch('manager.views.requests')
    def test_third_party_api_timeout(self, mock_requests):
        mock_requests.post.side_effect = Timeout()
        request = self.factory.post('/tickets/1/verify/',
                                    data=self.valid_ticket)
        response = VerifyTicketsView.as_view()(request, 1)
        self.assertEqual(response.status_code, 503)
        self.assertTrue(mock_requests.post.called)

    def test_invalid_ticket(self):
        request = self.factory.post('/tickets/1/verify/',
                                    data={})
        response = VerifyTicketsView.as_view()(request, 1)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['extraction'],
                         ['This field is required.'])
        self.assertEqual(response.data['number'],
                         ['This field is required.'])
        self.assertEqual(response.data['ruffle_date'],
                         ['This field is required.'])

    @patch('manager.views.requests')
    def test_third_party_returns_200_OK(self, mock_requests):
        mock_requests.post.return_value.status_code = 200
        mock_requests.post.return_value.ok = True
        request = self.factory.post('/tickets/1/verify/',
                                    data=self.valid_ticket)
        response = VerifyTicketsView.as_view()(request, 1)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(mock_requests.post.called)
        self.assertEqual(mock_requests.post.call_args_list,
                         [call('http://127.0.0.1:8001/tickets/1/verify/',
                               data=self.valid_ticket, timeout=1)])

    @patch('manager.views.requests')
    def test_third_party_returns_404_NOT_FOUND(self, mock_requests):
        mock_requests.post.return_value.status_code = 404
        mock_requests.post.return_value.ok = False
        request = self.factory.post('/tickets/1/verify/',
                                    data=self.valid_ticket)
        response = VerifyTicketsView.as_view()(request, 1)
        self.assertEqual(response.status_code, 404)
