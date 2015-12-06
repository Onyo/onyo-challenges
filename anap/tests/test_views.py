

def test_view_checkticket():
    from anap.powerball_checker.views import VerifyTicketView
    from rest_framework.test import APIRequestFactory
    #
    # factory = APIRequestFactory()
    # request = factory.post(
    #     'v1/power-ball/check/', {'title': 'new idea'}, format='json'
    # )
