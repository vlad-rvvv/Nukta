from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin_core/', admin.site.urls),
    path('', include('base.urls')),
    path('admin/', include('admin_panel.urls'))
]
