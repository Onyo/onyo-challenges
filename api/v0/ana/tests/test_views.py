# -*- coding: utf-8 -*-
from mock import patch

from django.core.urlresolvers import reverse
from django.test import LiveServerTestCase

from rest_framework import status
from rest_framework.test import APITestCase

from api.v0.ana.models import LottoTicket
from api.v0.ana.exceptions import BobTicketBadRequestException


class LottoTicketResultAPIViewTestCase(APITestCase, LiveServerTestCase):

    def setUp(self):
        self.url = reverse('ana:lotto_ticket_result')
        self.data = {'numbers': [1, 2, 3, 4, 5, 6]}

    def tearDown(self):
        LottoTicket.objects.all().delete()

    # Unit Tests

    @patch('api.v0.ana.views.LottoTicketSerializer')
    @patch('api.v0.ana.views.LottoTicketRepository')
    def test_unit__post_returns_200_OK_if_serializer_is_valid(self, mocked_repository, mocked_serializer):
        dummy_lotto_ticket = LottoTicket(is_winner=False, numbers=[1, 2, 3, 4, 5, 6])
        dummy_lotto_ticket.save()

        mocked_serializer().is_valid.return_value = True
        mocked_repository().get_by_numbers.return_value = dummy_lotto_ticket

        response = self.client.post(self.url, self.data, format='json')

        self.assertTrue(mocked_repository().get_by_numbers.called)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('id', response.content)
        self.assertIn('is_winner', response.content)
        self.assertIn('numbers', response.content)

    @patch('api.v0.ana.views.LottoTicketSerializer')
    def test_unit__post_returns_400_BAD_REQUEST_if_serializer_is_not_valid(self, mocked_serializer):
        mocked_serializer().is_valid.return_value = False
        mocked_serializer().errors = {'numbers': ['This field is required.']}

        response = self.client.post(self.url, {}, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content, '{"numbers":["This field is required."]}')

    @patch('api.v0.ana.views.LottoTicketSerializer')
    @patch('api.v0.ana.views.LottoTicketRepository')
    def test_unit__post_returns_400_BAD_REQUEST_if_repository_raises_bad_request_exception(self, mocked_repository, mocked_serializer):
        mocked_serializer().is_valid.return_value = True
        mocked_repository().get_by_numbers.side_effect = BobTicketBadRequestException

        response = self.client.post(self.url, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content, '{"reason":"Retrieving data from bob has failed."}')

    # Integration Tests

    def test_integration__post_returns_200_OK_if_serializer_is_valid(self):
        self.assertEqual(0, LottoTicket.objects.count())

        response = self.client.post(self.url, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('id', response.content)
        self.assertIn('is_winner', response.content)
        self.assertIn('numbers', response.content)
        self.assertEqual(1, LottoTicket.objects.count())

        response = self.client.post(self.url, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('id', response.content)
        self.assertIn('is_winner', response.content)
        self.assertIn('numbers', response.content)
        self.assertEqual(1, LottoTicket.objects.count())

    def test_integration__post_returns_400_BAD_REQUEST_if_serializer_is_not_valid(self):
        self.assertEqual(0, LottoTicket.objects.count())

        response = self.client.post(self.url, {}, format='json')

        self.assertEqual(0, LottoTicket.objects.count())
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content, '{"numbers":["This field is required."]}')
