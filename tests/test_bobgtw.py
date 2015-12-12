from powerball_checker.bobgtw import BobGateway


def test_valid_ticket(mock):
    requests = mock.patch("powerball_checker.bobgtw.requests")

    bob = BobGateway()

    requests.post.return_value.json.return_value = {'winner': False}
    assert not bob.is_a_winner_ticket('2015-09-01', "[1,2,3,4,5,6]")

    requests.post.return_value.json.return_value = {'winner': True}
    assert bob.is_a_winner_ticket('2015-09-01', "[1,2,3,4,5,6]")


def test_save(mock):
    requests = mock.patch("powerball_checker.bobgtw.requests")

    bob = BobGateway()

    requests.post.return_value.json.return_value = {
        'prize_code': '12312', 'ticket_code': '123123'}

    tkt = bob.create_ticket('2015-09-01', "[1,2,3,4,5,6]")

    assert tkt == {'prize_code': '12312', 'ticket_code': '123123'}
