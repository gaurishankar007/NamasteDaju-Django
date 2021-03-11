from django.shortcuts import render, redirect
from . models import Reservation
from django.contrib import messages


def home(request):
    dictionary = {'home': 'selected'}
    return render(request, 'Nd/Home.html', dictionary)


def menu(request):
    dictionary = {'menu': 'selected'}
    return render(request, 'Nd/Menu.html', dictionary)

def gallery(request):
    dictionary = {'gallery': 'selected'}
    return render(request, 'Nd/Gallery.html', dictionary)

def stories(request):
    dictionary = {'stories': 'selected'}
    return render(request, 'Nd/Stories.html', dictionary)

def reservation(request):
    if request.method == 'POST':
        form = request.POST
        reserve = Reservation.objects.create(name=form['name'], email=form['email'], phone=form['phone'], date=form['date'], time=form['time'], person=form['person'])
        if reserve:
            messages.add_message(request, messages.SUCCESS, 'You have booked a table successfully')
            return redirect('/Nd/reservation')
        else:
            messages.add_message(request, messages.ERROR, 'Failed to book a table')
            return render(request, 'Nd/Reservation.html', {'form': form})

    dictionary = {'form':Reservation, 'reservation': 'selected'}
    return render(request, 'Nd/Reservation.html', dictionary)

def catering(request):
    dictionary = {'catering': 'selected'}
    return render(request, 'Nd/Catering.html', dictionary)

def contact(request):
    dictionary = {'contact': 'selected'}
    return render(request, 'Nd/Contact.html', dictionary)
