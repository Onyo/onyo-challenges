from rest_framework import serializers


class TicketSerializer(serializers.Serializer):
    draw_date = serializers.DateField()
    ticket = serializers.JSONField()

    def winner(self):
        return self.validated_data["draw_date"].month == 9
