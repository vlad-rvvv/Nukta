from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home_page"),
    path('HIV-test/', views.service_1, name="HIV-test"),
    path('capillary-HIV-test/', views.service_2, name="capillary"),
    path('home-HIV-test/', views.service_3, name="home-HIV-test"),
    path('ART-HIV/', views.service_4, name="ART-HIV"),
    path('home-ART-HIV/', views.service_5, name="home-ART-HIV"),
    path('PEP-HIV/', views.service_6, name="PEP-HIV"),
    path('home-PEP-HIV/', views.service_7, name="home-PEP-HIV"),
    path('transport-HIV-test/', views.service_8, name="transport-HIV-test"),

    path('HIV-test/booking/<str:pk>/<str:year>/<str:month>/<str:day>', views.service_form_1, name="booking_page_1"),
    path('capillary-HIV-test/booking/<str:pk>/<str:year>/<str:month>/<str:day>', views.service_form_2, name="booking_page_2"),
    path('home-HIV-test/booking/<str:pk>/<str:year>/<str:month>/<str:day>', views.service_form_3, name="booking_page_3"),
    path('ART-HIV/booking/<str:pk>/<str:year>/<str:month>/<str:day>', views.service_form_4, name="booking_page_4"),
    path('home-ART-HIV/booking/<str:pk>/<str:year>/<str:month>/<str:day>', views.service_form_5, name="booking_page_5"),
    path('PEP-HIV/booking/<str:pk>/<str:year>/<str:month>/<str:day>', views.service_form_6, name="booking_page_6"),
    path('home-PEP-HIV/booking/<str:pk>/<str:year>/<str:month>/<str:day>', views.service_form_7, name="booking_page_7"),
    path('transport-HIV-test/booking/<str:pk>/<str:year>/<str:month>/<str:day>', views.service_form_8, name="booking_page_8"),
]
