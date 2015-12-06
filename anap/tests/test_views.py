from powerball_checker.views import VerifyTicketView
from django.test import RequestFactory
import json
from tests.utils import BootstrapViewTest


def test_verify_ticket(mock):
    ticket_mock = mock.patch("powerball_checker.views.TicketSerializer")
    ticket_mock.return_value.is_valid.return_value = True

    request = RequestFactory().post('/path', data={})

    tester = BootstrapViewTest()
    view = tester.setup_view(VerifyTicketView(), request)

    ticket_mock.return_value.winner.return_value = False
    response = json.loads(
        tester.dispatch_view(view).render().content.decode("utf-8")
    )
    assert not response['winner']

    ticket_mock.return_value.winner.return_value = True
    response = json.loads(
        tester.dispatch_view(view).render().content.decode("utf-8")
    )
    assert response['winner']
