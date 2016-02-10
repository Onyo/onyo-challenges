# -*- coding: utf-8 -*-

from core.serializers import LottoTicketSerializer as CoreLottoTicketSerializer
from api.v0.ana.models import LottoTicket


class LottoTicketSerializer(CoreLottoTicketSerializer):

    def create(self, validated_data):
        return LottoTicket.objects.create(**validated_data)
