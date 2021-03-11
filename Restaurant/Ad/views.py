from django.shortcuts import render, redirect
from django.contrib import messages


def home(request):
    return render(request, 'Ad/Admin.html')
