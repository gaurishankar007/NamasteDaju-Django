from django.shortcuts import render, redirect

from . models import *
from . forms import *
from . filters import MenuFilter, StoriesFilter

from django.contrib import messages
import os

from django.contrib.auth.decorators import login_required
from Ac.auth import user_only


@login_required
@user_only
def home(request):
    dictionary = {'home': 'selected'}
    return render(request, 'Nd/Home.html', dictionary)


@login_required
@user_only
def menu(request):
    menu = Menu.objects.all()
    menu_filter = MenuFilter(request.GET, queryset=menu)
    menu_final = menu_filter.qs
    dictionary = {'key': menu_final, 'menu_filter':menu_filter, 'menu': 'selected'}
    return render(request, 'Nd/Menu.html', dictionary)


@login_required
@user_only
def gallery(request):
    dictionary = {'key': Gallery.objects.all(), 'gallery': 'selected'}
    return render(request, 'Nd/Gallery.html', dictionary)


@login_required
@user_only
def stories(request):
    stories = Stories.objects.all()
    stories_filter = StoriesFilter(request.GET, queryset=stories)
    stories_final = stories_filter.qs
    dictionary = {'key': stories_final, 'stories_filter':stories_filter, 'stories': 'selected'}
    return render(request, 'Nd/Stories.html', dictionary)


@login_required
@user_only
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
@user_only
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
@user_only
def contact(request):
    dictionary = {'contact': 'selected'}
    return render(request, 'Nd/Contact.html', dictionary)
