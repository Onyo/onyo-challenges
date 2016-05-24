from datetime import date

from rest_framework import serializers

from .models import Tickets


class TicketsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tickets

    def validate_extraction(self, value):
        """Validate if extraction is higher than 1."""
        if value <= 0:
            raise serializers.ValidationError(
                "Extraction must be higher then 1"
            )
        return value

    def validate_number(self, value):
        """Validate if nuber is zero or until 6 digits."""
        if 0 > value or value > 999999:
            raise serializers.ValidationError(
                "Number must be between 0 and 999999"
            )
        return value

    def validate_ruffle_date(self, value):
        """Validate if ruffle date is less than value."""
        if value < date.today():
            raise serializers.ValidationError(
                "Ruffle already happened."
            )
        return value
