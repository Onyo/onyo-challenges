# -*- coding: utf-8 -*-
from django.conf.urls import url

from api.v0.bob.views import LottoTicketResultAPIView

urlpatterns = [
    url(r'$', LottoTicketResultAPIView.as_view(), name='lotto_ticket_result')
]
