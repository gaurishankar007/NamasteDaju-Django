from django.db import models
from django.core import validators


class Menu(models.Model):
    options = (('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Deserts', 'Deserts'), ('Wine Card', 'Wine Card'), ('Drinks & Tea', 'Drinks & Tea'))
    name = models.CharField(max_length=50, validators=[validators.MinLengthValidator(2)])
    description = models.CharField(max_length=200, validators=[validators.MinLengthValidator(4)])
    price = models.IntegerField()
    image = models.FileField(upload_to='static/images/uploads/menu')
    category = models.CharField(max_length=200, choices=options ,validators=[validators.MinLengthValidator(4)])
    uploaded_date = models.DateTimeField(auto_now_add=True)

class Gallery(models.Model):
    name = models.CharField(max_length=50, validators=[validators.MinLengthValidator(2)])
    image = models.FileField(upload_to='static/images/uploads/gallery')
    uploaded_date = models.DateTimeField(auto_now_add=True)

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=10)
    person = models.IntegerField()
    reserved_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name