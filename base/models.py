from django.db import models

TIME_CHOICES = [
    ("9:00", "9:00"),
    ("10:00", "10:00"),
    ("11:00", "11:00"),
    ("12:00", "12:00"),
    ("13:00", "13:00"),
    ("14:00", "14:00"),
    ("15:00", "15:00"),
    ("16:00", "16:00"),
    ("17:00", "17:00"),
    ("18:00", "18:00"),
]

SEX_CHOICES = [
    ("Мужской", "Мужской"),
    ("Женский", "Женский"),
]

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Booking(models.Model):
    title = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    sex = models.CharField(max_length=20, choices=SEX_CHOICES)
    birthday = models.CharField(max_length=3)
    address = models.CharField(max_length=200, blank=True)
    appointment_day = models.DateField(null=True, blank=True)
    appointment_time = models.CharField(max_length=20, choices=TIME_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name