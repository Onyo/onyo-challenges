# -*- coding: utf-8 -*-
import json

from api.v0.ana.models import LottoTicket
from api.v0.ana.services import get_bob_ticket_by_numbers


class LottoTicketRepository(object):

    def get_by_numbers(self, numbers):
        try:
            return LottoTicket.objects.get(numbers=numbers)
        except LottoTicket.DoesNotExist:
            encoded_ticket_data = get_bob_ticket_by_numbers(numbers)
            decoded_ticket_data = json.loads(encoded_ticket_data)
            ticket = LottoTicket.objects.create(**decoded_ticket_data)
            return ticket
