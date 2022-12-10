from django.shortcuts import render, redirect
from .models import Service
from .forms import BookingForm
import calendar
import datetime

def month_dates(pk):

    translate = {
        'January':'Январь',
        'February ':'Февраль',
        'March':'Март',
        'April':'Апрель',
        'May':'Май',
        'June':'Июнь',
        'July':'Июль',
        'August':'Август',
        'September':'Сентябрь',
        'October':'Октябрь',
        'November':'Ноябрь',
        'December':'Декабрь',
    }

     #Достаем услугу из бд
    service = Service.objects.get(id=pk)
    #Определяем текущий год и месяц (системы)
    now = datetime.datetime.now()
    year = now.year
    month = now.month

    #Используем календарь, вставляем в качестве параметров интересующее нас время
    cal = calendar.Calendar(firstweekday=0)
    month_days = cal.monthdayscalendar(year, month)

    #Перебираем полученный список из дат текущего месяца, создаем новый список
    dates = []
    for i in range(len(month_days)):
        for j in range(len(month_days[i])):
            dates.append(month_days[i][j])
    
    month_name = calendar.month_name[month]
    month_translate = translate[str(month_name)]
    context = {'service':service, 'dates':dates, 'year':year, 'month':month, 'month_translate':month_translate}
    return context

def home(request):
    return render(request, 'index.html')

def service_1(request):
    context = month_dates(1)
    return render(request, 'service_1.html', context)
    
def service_2(request):
    context = month_dates(2)
    return render(request, 'service_2.html', context)

def service_3(request):
    context = month_dates(3)
    return render(request, 'service_3.html', context)

def service_4(request):
    context = month_dates(4)
    return render(request, 'service_4.html', context)

def service_5(request):
    context = month_dates(5)
    return render(request, 'service_5.html', context)

def service_6(request):
    context = month_dates(6)
    return render(request, 'service_6.html', context)

def service_7(request):
    context = month_dates(7)
    return render(request, 'service_7.html', context)

def service_8(request):
    context = month_dates(8)
    return render(request, 'service_8.html', context)

def service_form_1(request, pk, year, month, day):
    appointment_day = year+'-'+month+'-'+day
    service = Service.objects.get(id=pk)
    form = BookingForm()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.title = service
            booking.appointment_day = appointment_day
            booking.save()
            return redirect('home_page')
    
    context={'form':form}
    return render(request, 'service_with_form_1.html', context)

def service_form_2(request, pk, year, month, day):
    appointment_day = year+'-'+month+'-'+day
    service = Service.objects.get(id=pk)
    form = BookingForm()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.title = service
            booking.appointment_day = appointment_day
            booking.save()
            return redirect('home_page')
    
    context={'form':form}
    return render(request, 'service_with_form_2.html', context)

def service_form_3(request, pk, year, month, day):
    appointment_day = year+'-'+month+'-'+day
    service = Service.objects.get(id=pk)
    form = BookingForm()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.title = service
            booking.appointment_day = appointment_day
            booking.save()
            return redirect('home_page')
    
    context={'form':form}
    return render(request, 'service_with_form_3.html', context)

def service_form_4(request, pk, year, month, day):
    appointment_day = year+'-'+month+'-'+day
    service = Service.objects.get(id=pk)
    form = BookingForm()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.title = service
            booking.appointment_day = appointment_day
            booking.save()
            return redirect('home_page')
    
    context={'form':form}
    return render(request, 'service_with_form_4.html', context)

def service_form_5(request, pk, year, month, day):
    appointment_day = year+'-'+month+'-'+day
    service = Service.objects.get(id=pk)
    form = BookingForm()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.title = service
            booking.appointment_day = appointment_day
            booking.save()
            return redirect('home_page')
    
    context={'form':form}
    return render(request, 'service_with_form_5.html', context)

def service_form_6(request, pk, year, month, day):
    appointment_day = year+'-'+month+'-'+day
    service = Service.objects.get(id=pk)
    form = BookingForm()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.title = service
            booking.appointment_day = appointment_day
            booking.save()
            return redirect('home_page')
    
    context={'form':form}
    return render(request, 'service_with_form_6.html', context)

def service_form_7(request, pk, year, month, day):
    appointment_day = year+'-'+month+'-'+day
    service = Service.objects.get(id=pk)
    form = BookingForm()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.title = service
            booking.appointment_day = appointment_day
            booking.save()
            return redirect('home_page')
    
    context={'form':form}
    return render(request, 'service_with_form_7.html', context)

def service_form_8(request, pk, year, month, day):
    appointment_day = year+'-'+month+'-'+day
    service = Service.objects.get(id=pk)
    form = BookingForm()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.title = service
            booking.appointment_day = appointment_day
            booking.save()
            return redirect('home_page')
    
    context={'form':form}
    return render(request, 'service_with_form_8.html', context)