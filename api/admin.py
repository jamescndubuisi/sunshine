from django.contrib import admin

# Register your models here.
from .models import GPAppointment, Discount, Bill
admin.site.register(GPAppointment)
admin.site.register(Discount)
admin.site.register(Bill)
