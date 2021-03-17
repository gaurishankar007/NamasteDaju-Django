from django.shortcuts import render, redirect

from . models import *
from . forms import *

from django.contrib import messages
import os

from django.contrib.auth.decorators import login_required

def home(request):
    dictionary = {'home': 'selected'}
    return render(request, 'Nd/Home.html', dictionary)


def menu(request):
    dictionary = {'key': Menu.objects.all(), 'menu': 'selected'}
    return render(request, 'Nd/Menu.html', dictionary)


def gallery(request):
    dictionary = {'key': Gallery.objects.all(), 'gallery': 'selected'}
    return render(request, 'Nd/Gallery.html', dictionary)


def stories(request):
    dictionary = {'key': Stories.objects.all(), 'stories': 'selected'}
    return render(request, 'Nd/Stories.html', dictionary)


@login_required
def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'You have booked table successfully')
            return redirect('/Nd/reservation')
        else:
            messages.add_message(request, messages.ERROR, 'Failed to book table')
            return render(request, 'Nd/Reservation.html', {'form': form})
    dictionary = {'form':ReservationForm, 'reservation': 'selected'}
    return render(request, 'Nd/Reservation.html', dictionary)


@login_required
def catering(request):
    if request.method == 'POST':
        form = CateringForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'You have ordered catering successfully')
            return redirect('/Nd/catering')
        else:
            messages.add_message(request, messages.ERROR, 'Failed to order catering')
            return render(request, 'Nd/catering.html', {'form': form})
    dictionary = {'form':CateringForm ,'catering': 'selected'}
    return render(request, 'Nd/Catering.html', dictionary)


@login_required
def contact(request):
    dictionary = {'contact': 'selected'}
    return render(request, 'Nd/Contact.html', dictionary)
