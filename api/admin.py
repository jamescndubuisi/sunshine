from django.contrib import admin

# Register your models here.
from .models import GPAppointment, Discount
admin.site.register(GPAppointment)
admin.site.register(Discount)
