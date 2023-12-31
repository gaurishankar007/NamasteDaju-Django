from django import forms
from django.forms import ModelForm
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user', 'username', 'staff']
        widgets = {'phone':  forms.widgets.TextInput(attrs={'onkeypress': 'validate(event)'})}