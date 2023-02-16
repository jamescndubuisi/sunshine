from rest_framework import serializers
from .models import GPAppointment, Discount


class GPAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPAppointment
        fields = ["date", "time", "location", "doctor", "message"]


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ["source", "amount", "message", "updated", "user"]
