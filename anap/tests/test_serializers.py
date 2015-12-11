from powerball_checker.serializers import TicketSerializer


def test_is_winner(mock):
    bob = mock.patch('powerball_checker.serializers.BobGateway')
    bob.return_value.is_a_winner_ticket.return_value = True

    t = TicketSerializer(
        data={'ticket': '[1,2,4,5]', 'draw_date': '2015-1-15'}
    )

    assert t.is_valid()
    assert t.winner()

    bob.return_value.is_a_winner_ticket.assert_called_with(
        "15/01/2015", "[1,2,4,5]"
    )
