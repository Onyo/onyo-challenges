from django.conf import settings
import requests


class BobGateway:

    def is_a_winner_ticket(self, draw_date, ticket):
        ticket = requests.post(
            'http://{}/power-ball-core/v1/check-winner/'.format(settings.BOB_URL),
            data={'ticket': ticket, 'draw_date': draw_date}
        ).json()

        return ticket['winner']
