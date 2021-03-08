from django.db import models
from django.core import validators


class Menu(models.Model):
    name = models.CharField(max_length=50, validators=[validators.MinLengthValidator(2)])
    description = models.CharField(max_length=200, validators=[validators.MinLengthValidator(4)])
    price = models.IntegerField()
    image = models.FileField(upload_to='static/uploads/menus')
    category = models.CharField(max_length=200, validators=[validators.MinLengthValidator(4)])
    created_date = models.DateTimeField(auto_now_add=True)
