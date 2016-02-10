# -*- coding: utf-8 -*-

from rest_framework import serializers


def lotto_ticket_number_validator(value):
    if len(value) != 6:
        raise serializers.ValidationError('This field requires a list of exactly six numbers.')


class LottoTicketSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    is_winner = serializers.BooleanField(required=False)
    numbers = serializers.ListField(
        child=serializers.IntegerField(min_value=1, max_value=60),
        validators=[lotto_ticket_number_validator]
    )
