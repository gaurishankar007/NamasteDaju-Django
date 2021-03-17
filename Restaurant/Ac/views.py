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
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                if not user.is_staff:
                    login(request, user)
                    return redirect('/Nd/home')
                elif user.is_staff:
                    login(request, user)
                    return redirect('/Ad/admin')
            else:
                messages.add_message(request, messages.ERROR, 'Username or Password Invalid')
                return render(request, 'Ac/Login.html', {'form': form})
    dictionary = {'form': LoginForm}
    return render(request, 'Ac/Login.html', dictionary)

def logout_user(request):
    logout(request)
    return redirect('/Nd/home')