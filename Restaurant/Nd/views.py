from django.shortcuts import render


def home(request):
    dictionary = {'home': 'selected'}
    return render(request, 'Nd/Home.html', dictionary)


def menu(request):
    dictionary = {'menu': 'selected'}
    return render(request, 'Nd/Menu.html', dictionary)
