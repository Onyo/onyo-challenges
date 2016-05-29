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


class UserTicketsSerializer(serializers.Serializer):
    extraction = serializers.IntegerField(min_value=1)
    number = serializers.IntegerField(min_value=0, max_value=999999)
    ruffle_date = serializers.DateField()
