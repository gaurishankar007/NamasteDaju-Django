from django import forms
from django.forms import ModelForm
from .models import *
from datetime import date


class MenuForm(ModelForm):
     class Meta:
        model = Menu
        fields = ['name', 'description', 'price', 'image', 'category']


class OrderForm(ModelForm):
   class Meta:
      model = Order
      fields = ['phone', 'quantity', 'address']
      widgets = {'phone':  forms.widgets.TextInput(attrs={'onkeypress': 'validate(event)'})}


class CartForm(ModelForm):
   class Meta:
      model = Cart
      fields = ['phone', 'address']
      widgets = {'phone':  forms.widgets.TextInput(attrs={'onkeypress': 'validate(event)'})}


class GalleryForm(ModelForm):
     class Meta:
        model = Gallery
        fields = ['name','image']


class StoriesForm(ModelForm):
   class Meta:
      model = Stories
      fields = ['name','image', 'detail']


class ReservationForm(ModelForm):
   class Meta:
      model = Reservation
      fields = ['username', 'firstname', 'lastname', 'email', 'phone', 'date', 'time', 'person']
      widgets = {'date': forms.widgets.DateInput(attrs={'type': 'date', 'min': date.today()}), 'time':  forms.widgets.TimeInput(attrs={'type': 'time'}),  
                  'phone':  forms.widgets.TextInput(attrs={'onkeypress': 'validate(event)'})}


class CateringForm(ModelForm):
   class Meta:
      model = Catering
      fields = ['username', 'firstname', 'lastname', 'email', 'phone', 'date', 'time', 'event_type', 'catering_type', 'address']
      widgets = {'date': forms.widgets.DateInput(attrs={'type': 'date', 'min': date.today()}), 'time':  forms.widgets.TimeInput(attrs={'type': 'time'}), 
                  'phone':  forms.widgets.TextInput(attrs={'onkeypress': 'validate(event)'})}


class MessageForm(ModelForm):
   class Meta:
      model = Message
      fields = ['username', 'subject', 'messages']