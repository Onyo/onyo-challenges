# -*- coding: utf-8 -*-
import json
from mock import patch

from django.conf import settings
from django.test import TestCase

from api.v0.ana.services import get_bob_ticket_by_numbers
from api.v0.ana.exceptions import BobTicketBadRequestException


class GetBobTicketByNumbersTestCase(TestCase):

    @patch('api.v0.ana.services.urllib2.urlopen')
    @patch('api.v0.ana.services.urllib2.Request')
    def test_service(self, mocked_request, mocked_urlopen):
        expected_data = json.dumps({'numbers': [1, 2]})

        response = get_bob_ticket_by_numbers([1, 2])

        self.assertTrue(mocked_request.called_once_with(settings.CURRENT_BOB_API_URL))
        self.assertTrue(mocked_request().add_header.called_once_with('Content-Type', 'application/json'))
        self.assertTrue(mocked_urlopen.called_once_with(mocked_request(), expected_data))
        self.assertEqual(response, mocked_urlopen().read())

    @patch('api.v0.ana.services.urllib2.urlopen')
    def test_service_raises_exception_if_bad_request_is_made(self, mocked_urlopen):
        mocked_urlopen.side_effect = BobTicketBadRequestException

        self.assertRaises(BobTicketBadRequestException, get_bob_ticket_by_numbers, [1, 2])
