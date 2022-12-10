from .models import Booking
from django.forms import ModelForm, TextInput

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['name','birthday','sex', 'phone_number', 'address', 'appointment_time']

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Имя'}),
            'birthday': TextInput(attrs={'placeholder': 'Возраст'}),
            'phone_number': TextInput(attrs={'placeholder': 'Номер телефона'}),
            'address': TextInput(attrs={'placeholder': 'Адрес'}),
        }