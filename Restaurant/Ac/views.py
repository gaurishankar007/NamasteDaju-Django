from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm


def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'You have been registered Successfully')
            return redirect('/Ac')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to Register You')
            return render(request, 'Ac/Register.html', {'form': form})
    dictionary = {'form': UserCreationForm}
    return render(request, 'Ac/Register.html', dictionary)


def login_user(request):
    form = LoginForm
    dictionary = {'form': form}
    return render(request, 'Nd/Home.html', dictionary)

def logout_user(request):
    logout(request)
    return redirect('/Ac')