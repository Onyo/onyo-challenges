# -*- coding: utf-8 -*-
import json
import urllib2

from django.conf import settings

from api.v0.ana.exceptions import BobTicketBadRequestException


def get_bob_ticket_by_numbers(numbers):
    try:
        data = json.dumps({'numbers': numbers})

        request = urllib2.Request(settings.CURRENT_BOB_API_URL)
        request.add_header('Content-Type', 'application/json')

        response = urllib2.urlopen(request, data)
        return response.read()
    except:
        raise BobTicketBadRequestException
