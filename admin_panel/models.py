from django.db import models
from base.models import Service
from base.models import SEX_CHOICES, TIME_CHOICES

class DeletedModels(models.Model):
    title = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    sex = models.CharField(max_length=20, choices=SEX_CHOICES)
    birthday = models.CharField(max_length=3)
    address = models.CharField(max_length=200, blank=True)
    appointment_day = models.DateField()
    appointment_time = models.CharField(max_length=20, choices=TIME_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
