from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_panel, name="admin_panel"),
    path('login/', views.login_page, name="login_page"),
    path('logout/', views.logoutUser, name="logout"),
    path('delete_booking/<str:pk>', views.delete_booking, name="delete_booking"),
    path('trash_can', views.trash_can, name="trash_can"),
    path('trash_delete/<str:pk>', views.trash_delete, name="trash_delete"),
    path('booking/<str:pk>', views.booking_profile, name="booking"),
    path('trash_booking/<str:pk>', views.trash_profile, name="trash_booking"),
    path('trash_reset/<str:pk>', views.reset_booking, name="trash_reset")
]
