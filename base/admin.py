from django.contrib import admin
from .models import Booking, Service
from admin_panel.models import DeletedModels

admin.site.register(Service)
admin.site.register(Booking)
admin.site.register(DeletedModels)