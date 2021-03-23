from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from .auth import *
from .models import Profile
from .forms import ProfileForm
from Nd.models import Order, Reservation, Catering, Message


@unauthenticated_user
def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, username=user.username)
            messages.add_message(request, messages.SUCCESS, 'You have been registered Successfully')
            return redirect('/Ac')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to Register You')
            return render(request, 'Ac/Register.html', {'form': form})
    dictionary = {'form': UserCreationForm}
    return render(request, 'Ac/Register.html', dictionary)


@unauthenticated_user
def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                if not user.is_staff:
                    login(request, user)
                    return redirect('/')
                elif user.is_staff:
                    login(request, user)
                    return redirect('/Ad/admin')
            else:
                messages.add_message(request, messages.ERROR, 'Username or Password Invalid')
                return render(request, 'Ac/Login.html', {'form': form})
    dictionary = {'form': LoginForm}
    return render(request, 'Ac/Login.html', dictionary)


@login_required
def user_account(request):
    order = None
    reservation = None
    catering = None
    message = None
    for i in Order.objects.all():
        if str(i.username) == str(request.user.username):
           order = i
    for j in Reservation.objects.all():
        if str(i.username) == str(request.user.username):
            reservation = j   
    for k in Catering.objects.all():
        if str(i.username) == str(request.user.username):
           catering = k   
    for l in Message.objects.all():
        if str(i.username) == str(request.user.username):
           message = l

    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Account Updated Successfully for "+str(request.user.profile.username))
            return redirect('/Ac/profile')
        else:
            messages.add_message(request, messages.ERROR, "Failed Updated Account for "+str(request.user.profile.username))
            return render(request, 'Ac/Profile.html', {'form': form, 'order':order, 'reservation':reservation, 'catering':catering, 'message':message})
    dictionary = {'form': form, 'order':order, 'reservation':reservation, 'catering':catering, 'message':message, 'underlined':'underlined'}
    return render(request, 'Ac/Profile.html', dictionary)


def logout_user(request):
    logout(request)
    return redirect('/')
