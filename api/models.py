from django.db import models

# Create your models here.


class GPAppointment(models.Model):
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    doctor = models.CharField(max_length=200)
    seen = models.BooleanField(default=False)
    message = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"GP Appointment: {self.doctor} {self.date} {self.time}"


class Discount(models.Model):
    amount = models.FloatField()
    source = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    seen = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"Discount {self.amount} {self.source}"


class Bill(models.Model):
    amount = models.FloatField()
    source = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    seen = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"Bill: {self.amount} {self.source}"
