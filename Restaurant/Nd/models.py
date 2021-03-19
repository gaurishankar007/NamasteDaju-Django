from django.db import models
from django.core import validators


class Menu(models.Model):
    options = (('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Deserts', 'Deserts'), ('Wine Card', 'Wine Card'), ('Drinks & Tea', 'Drinks & Tea'))
    name = models.CharField(max_length=50, validators=[validators.MinLengthValidator(2)], null=True)
    description = models.CharField(max_length=200, validators=[validators.MinLengthValidator(4)], null=True)
    price = models.IntegerField(null=True)
    image = models.FileField(upload_to='static/images/uploads/menu')
    category = models.CharField(max_length=200, choices=options ,validators=[validators.MinLengthValidator(4)], null=True)
    uploaded_date = models.DateTimeField(auto_now_add=True, null=True)


class Gallery(models.Model):
    name = models.CharField(max_length=50, validators=[validators.MinLengthValidator(2)], null=True)
    image = models.FileField(upload_to='static/images/uploads/gallery')
    uploaded_date = models.DateTimeField(auto_now_add=True, null=True)


class Stories(models.Model):
    name = models.CharField(max_length=50, validators=[validators.MinLengthValidator(2)], null=True)
    image = models.FileField(upload_to='static/images/uploads/stories')
    detail = models.TextField(max_length=2000, validators=[validators.MinLengthValidator(50)], null=True)
    uploaded_date = models.DateTimeField(auto_now_add=True, null=True)


class Reservation(models.Model):
    options = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'))
    firstname = models.CharField(max_length=100, validators=[validators.MinLengthValidator(2)], null=True)
    lastname = models.CharField(max_length=100, validators=[validators.MinLengthValidator(2)], null=True)
    email = models.EmailField(validators=[validators.EmailValidator], null=True)
    phone = models.CharField(max_length=10, validators=[validators.MinLengthValidator(10)], null=True)
    date = models.DateField(max_length=20, null=True)
    time = models.TimeField(max_length=10, null=True)
    person = models.CharField(max_length=2, choices=options, null=True)
    completion = models.BooleanField(default=False, null=True)
    reserved_date = models.DateTimeField(auto_now_add=True, null=True)


class Catering(models.Model):
    options1 = (('Weddings', 'Weddings'), ('Birthday Parties', 'Birthday Parties'), ('Anniversary Parties', 'Anniversary Parties'), ('Business Meetings', 'Business Meetings'),
                ('Conferences', 'Conferences'), ('Luncheons', 'Luncheons'), ('Holiday Gatherings', 'Holiday Gatherings'), ('Other', 'Other'))
    options2 = (('On-promise', 'On-promise'), ('Off-promise', 'Off-promise'))
    firstname = models.CharField(max_length=100, validators=[validators.MinLengthValidator(2)], null=True)
    lastname = models.CharField(max_length=100, validators=[validators.MinLengthValidator(2)], null=True)
    email = models.EmailField(validators=[validators.EmailValidator], null=True)
    phone = models.CharField(max_length=10, validators=[validators.MinLengthValidator(10)], null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    event_type = models.CharField(max_length=50, choices=options1, null=True)
    catering_type = models.CharField(max_length=50, choices=options2, null=True)
    address = models.CharField(blank=True, max_length=50, validators=[validators.MinLengthValidator(10)], null=True)
    completion = models.BooleanField(default=False, null=True)
    catering_order_date = models.DateTimeField(auto_now_add=True, null=True)



class Message(models.Model):
    subject = models.CharField(max_length=50, validators=[validators.MinLengthValidator(2)], null=True)
    messages = models.TextField(max_length=2000, validators=[validators.MinLengthValidator(50)], null=True)
    messaged_date = models.DateTimeField(auto_now_add=True, null=True)