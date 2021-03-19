from django.db import models
from django.core import validators
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100, validators=[validators.MinLengthValidator(2)], null=True)
    lastname = models.CharField(max_length=100, validators=[validators.MinLengthValidator(2)], null=True)
    username = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True, unique=True)
    phone = models.CharField(max_length=10, validators=[validators.MinLengthValidator(10)], null=True)
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')))
    profile_pic = models.FileField(upload_to='static/images/uploads/profiles', default='static/images/uploads/profiles/default_profile.jpg')
    created_date = models.DateTimeField(auto_now_add=True, null=True)