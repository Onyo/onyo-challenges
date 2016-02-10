# -*- coding: utf-8 -*-
import json
from mock import patch

from django.test import TestCase

from api.v0.ana.models import LottoTicket
from api.v0.ana.repositories import LottoTicketRepository


class LottoTicketRepositoryTestCase(TestCase):

    def setUp(self):
        self.repository = LottoTicketRepository()

    def tearDown(self):
        LottoTicket.objects.all().delete()

    def test_get_by_numbers_with_ticket_in_db(self):
        ticket = LottoTicket(is_winner=True, numbers=[1, 2])
        ticket.save()
        self.assertEqual(self.repository.get_by_numbers([1, 2]), ticket)

    @patch('api.v0.ana.repositories.get_bob_ticket_by_numbers')
    def test_get_by_numbers_without_ticket_in_db(self, mocked_service):
        mocked_service.return_value = json.dumps({'is_winner': True, 'numbers': [1, 2]})
        self.assertEqual(0, LottoTicket.objects.count())

        ticket = self.repository.get_by_numbers([1, 2])

        self.assertEqual(1, LottoTicket.objects.count())
        self.assertEqual(LottoTicket.objects.all()[0], ticket)
