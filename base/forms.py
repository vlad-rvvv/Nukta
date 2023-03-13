from .models import Booking
from admin_panel.models import DeletedModels
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


class BookingAdminForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Имя'}),
            'birthday': TextInput(attrs={'placeholder': 'Возраст'}),
            'phone_number': TextInput(attrs={'placeholder': 'Номер телефона'}),
            'address': TextInput(attrs={'placeholder': 'Адрес'}),
            'appointment_day': TextInput(attrs={'placeholder':'День записи в формате дд-мм-гггг'})
        }

class DeletedModelsForm(ModelForm):
    class Meta:
        model = DeletedModels
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Имя'}),
            'birthday': TextInput(attrs={'placeholder': 'Возраст'}),
            'phone_number': TextInput(attrs={'placeholder': 'Номер телефона'}),
            'address': TextInput(attrs={'placeholder': 'Адрес'}),
            'appointment_day': TextInput(attrs={'placeholder':'День записи в формате дд-мм-гггг'})
        }