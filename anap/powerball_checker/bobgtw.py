from django.conf import settings
import requests


class BobGateway:

    def is_a_winner_ticket(self, draw_date, ticket):
        ticket = requests.post(
            'http://{}/power-ball-core/v1/ticket/check-winner/'.format(settings.BOB_URL),
            data={'ticket': ticket, 'draw_date': draw_date}
        ).json()

        return ticket['winner']

    def create_ticket(self, draw_date, ticket):
        ticket = requests.post(
            'http://{}/power-ball-core/v1/ticket/create'.format(settings.BOB_URL),
            data={'ticket': ticket, 'draw_date': draw_date}
        ).json()

        return {
            'prize_code': ticket['prize_code'],
            'ticket_code': ticket['ticket_code']
        }
