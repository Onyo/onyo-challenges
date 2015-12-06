import requests


# def test_winning_numbers():
#     winning_ticket = "[1,2,3,4,5,6]"
#     draw_date = "2015-09-01"
#
#     ticket = requests.post(
#         'http://localhost:5000/power-ball/v1/check/',
#         data={'ticket': winning_ticket, 'draw_date': draw_date}
#     ).json()
#
#     assert ticket['winner']
