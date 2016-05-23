from datetime import date

from rest_framework import serializers

from .models import Ticket


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket

    def validate_extraction(self, value):
        """Validate if extraction is higher than 1."""
        if value <= 0:
            raise serializers.ValidationError(
                "Extraction must be higher then 1"
            )
        return value

    def validate_number(self, value):
        """Validate if nuber is higher than 1 and until 6 digits."""
        if 0 > value >= 999999:
            raise serializers.ValidationError(
                "Number must be higher then 1"
            )
        return value

    def validate_ruffle_date(self, value):
        """Validate if ruffle date is less than value."""
        if value < date.today():
            raise serializers.ValidationError(
                "Ruffle already happened."
            )
        return value
