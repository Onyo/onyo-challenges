from powerball_checker.serializers import TicketSerializer


def test_not_acess_bob(mock):
    bob = mock.patch('powerball_checker.serializers.BobGateway')
    model_ticket = mock.patch('powerball_checker.serializers.Ticket')

    object_ticket = mock.Mock()
    object_ticket.drawed.return_value = True
    object_ticket.winning = False
    model_ticket.objects.filter.return_value = [object_ticket]

    t = TicketSerializer(
        data={'ticket': '[1,2,4,5]', 'draw_date': '2015-1-15'}
    )

    assert t.is_valid()
    assert t.winner() is False

    bob.return_value.is_a_winner_ticket.assert_not_called()


def test_accessing_bob(mock):
    bob = mock.patch('powerball_checker.serializers.BobGateway')
    model_ticket = mock.patch('powerball_checker.serializers.Ticket')

    object_ticket = mock.Mock()
    object_ticket.drawed.return_value = False
    model_ticket.objects.filter.return_value = [object_ticket]

    bob.return_value.is_a_winner_ticket.return_value = True

    t = TicketSerializer(
        data={'ticket': '[1,2,4,5]', 'draw_date': '2015-1-15'}
    )

    assert t.is_valid()
    assert t.winner()

    bob.return_value.is_a_winner_ticket.assert_called_with(
        "15/01/2015", "[1,2,4,5]"
    )


def test_create(mock):
    bob = mock.patch('powerball_checker.serializers.BobGateway')
    bob.return_value.create.return_value = {
        'prize_code': '12312', 'ticket_code': '123123'}

    model_ticket = mock.patch('powerball_checker.serializers.Ticket')
    model_prize = mock.patch('powerball_checker.serializers.Prize')

    t = TicketSerializer(
        data={'ticket': '[1,2,4,5]', 'draw_date': '2015-1-15'}
    )

    assert t.is_valid()

    t.save()
    model_ticket.return_value.save.assert_called_with()
    model_prize.return_value.save.assert_called_with()
