import requests
import datetime


def test_winning_numbers():
    winning_ticket = "1,2,3,4,5,6"
    draw_date = datetime.datetime(2015, 9, 1)

    ticket = requests.post(
        'http://localhost:5000/v1/power-ball/check/',
        data={'ticket': winning_ticket, 'draw-date': draw_date}
    ).json()

    assert ticket['winner'], False
