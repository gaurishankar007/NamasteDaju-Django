from django import forms
from django.forms import ModelForm
from .models import Menu, Reservation

class MenuForm(ModelForm):
     class Meta:
        model = Menu
        fields = '__all__'
