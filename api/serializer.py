from rest_framework import serializers
from .models import GPAppointment, Discount, Bill


class GPAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPAppointment
        fields = ["date", "time", "location", "doctor", "message", "seen"]


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ["source", "amount", "message", "updated", "seen"]


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ["source", "amount", "message", "updated", "seen"]
