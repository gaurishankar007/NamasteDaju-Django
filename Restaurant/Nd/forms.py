from django import forms
from django.forms import ModelForm
from .models import Menu, Gallery

class MenuForm(ModelForm):
     class Meta:
        model = Menu
        fields = ['name', 'description', 'price', 'image', 'category']

class GalleryForm(ModelForm):
     class Meta:
        model = Gallery
        fields = ['name','image']
