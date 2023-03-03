from django.shortcuts import render, redirect

#импорты для аутентификации 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#импорты моделей
from django.contrib.auth.models import User
from base.models import Booking, Service
from .models import DeletedModels

#импорты форм
from base.forms import BookingAdminForm, BookingForm, DeletedModelsForm

#импорт системы поиска
from django.db.models import Q


@login_required(login_url='login_page')
def admin_panel(request):

    # Фильрация поиска
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    booking_list = Booking.objects.filter(
        Q(name__icontains=q) |
        Q(phone_number__icontains=q)
        )

    booking_form = BookingAdminForm()
    if request.method == 'POST':
        booking_form = BookingAdminForm(request.POST)
        if booking_form.is_valid():
            booking_form.save()
            return redirect('admin_panel')

    context = {'booking_list':booking_list, 'booking_form':booking_form}
    return render(request, 'admin_panel.html', context)

def login_page(request):
     # Аутентификация
    if request.method == 'POST':
        # С инпутов принимается информация по атрибуту name
        username = request.POST.get('username')
        password = request.POST.get('password')   
        # Поиск пользователя с идентичным именем
        try:
            user = User.objects.get(username=username)
        except:
            pass
        # Функция аутентификации
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_panel')

    return render(request, 'login_page.html')

def logoutUser(request):
    logout(request)
    return redirect('login_page')

def delete_booking(request, pk):
    booking = Booking.objects.get(id=pk)
    title = booking.title
    name = booking.name
    phone_number = booking.phone_number
    sex = booking.sex
    birthday = booking.birthday
    address = booking.address
    appointment_day = booking.appointment_day
    appointment_time = booking.appointment_time
    DeletedModels.objects.create(
        title = title,
        name = name,
        phone_number = phone_number,
        sex = sex,
        birthday = birthday,
        address = address,
        appointment_day = appointment_day,
        appointment_time = appointment_time
        )
    booking.delete()
    return redirect('admin_panel')

def trash_can(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    trash_booking = DeletedModels.objects.filter(
        Q(name__icontains=q) |
        Q(phone_number__icontains=q)
        )
    context = {'trash_booking':trash_booking}
    return render(request, 'trash_can.html', context)

def trash_delete(request, pk):
    trash_obj = DeletedModels.objects.get(id=pk)
    trash_obj.delete()
    return redirect('trash_can')

def booking_profile(request, pk):
    booking = Booking.objects.get(id=pk)
    booking_form = BookingAdminForm(instance=booking)
    booking_list = Booking.objects.all()

    if request.method == "POST":
        title = request.POST.get("title")
        title = Service.objects.get(id=title)
        booking.title = title
        booking.name = request.POST.get("name")
        booking.phone_number = request.POST.get("phone_number")
        booking.sex = request.POST.get("sex")
        booking.birthday = request.POST.get("birthday")
        booking.address = request.POST.get("address")
        booking.appointment_day = request.POST.get("appointment_day")
        booking.appointment_time = request.POST.get("appointment_time")
        booking.save()
        return redirect('booking', str(booking.id))

    context = {"booking":booking, 'booking_form':booking_form, 'booking_list':booking_list}
    return render(request, "booking_profile.html", context)

def trash_profile(request, pk):
    booking = DeletedModels.objects.get(id=pk)
    booking_form = DeletedModelsForm(instance=booking)
    booking_list = DeletedModels.objects.all()

    if request.method == "POST":
        title = request.POST.get("title")
        title = Service.objects.get(id=title)
        booking.title = title
        booking.name = request.POST.get("name")
        booking.phone_number = request.POST.get("phone_number")
        booking.sex = request.POST.get("sex")
        booking.birthday = request.POST.get("birthday")
        booking.address = request.POST.get("address")
        booking.appointment_day = request.POST.get("appointment_day")
        booking.appointment_time = request.POST.get("appointment_time")
        booking.save()
        return redirect('booking', str(booking.id))

    context = {"booking":booking, 'booking_form':booking_form, 'booking_list':booking_list}
    return render(request, "trash_profile.html", context)

def reset_booking(request, pk):
    booking = DeletedModels.objects.get(id=pk)
    title = booking.title
    name = booking.name
    phone_number = booking.phone_number
    sex = booking.sex
    birthday = booking.birthday
    address = booking.address
    appointment_day = booking.appointment_day
    appointment_time = booking.appointment_time
    Booking.objects.create(
        title = title,
        name = name,
        phone_number = phone_number,
        sex = sex,
        birthday = birthday,
        address = address,
        appointment_day = appointment_day,
        appointment_time = appointment_time
        )
    booking.delete()
    return redirect('trash_can')