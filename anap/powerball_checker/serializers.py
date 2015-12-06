from rest_framework import serializers
from powerball_checker.bobgtw import BobGateway


class TicketSerializer(serializers.Serializer):
    draw_date = serializers.DateField()
    ticket = serializers.JSONField()

    def winner(self):
        # return self.validated_data["draw_date"].month == 9
        return BobGateway().is_a_winner_ticket(
            self.cleaned_data["draw_date"],
            self.cleaned_data["ticket"],
        )
