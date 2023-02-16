from django.shortcuts import render, HttpResponse
from rest_framework.generics import ListAPIView
from .models import Discount, GPAppointment
from .serializer import DiscountSerializer, GPAppointmentSerializer
from rest_framework.views import APIView

# Create your views here.


def home(request):
    return HttpResponse({"name": "name"})


class GPListAPIView(ListAPIView):
    queryset = GPAppointment.objects.all()
    serializer_class = GPAppointmentSerializer


class GPListUnseenAPIView(ListAPIView):
    queryset = GPAppointment.objects.filter(seen=False)
    serializer_class = GPAppointmentSerializer


class GPListSeenAPIView(ListAPIView):
    queryset = GPAppointment.objects.filter(seen=True)
    serializer_class = GPAppointmentSerializer


class DiscountListAPIView(ListAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


class DiscountListUnseenAPIView(ListAPIView):
    queryset = Discount.objects.filter(seen=False)
    serializer_class = DiscountSerializer


class DiscountListSeenAPIView(ListAPIView):
    queryset = Discount.objects.filter(seen=True)
    serializer_class = DiscountSerializer


