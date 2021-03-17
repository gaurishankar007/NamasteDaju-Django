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

    def __str__(self):
        return self.name


class Gallery(models.Model):
    name = models.CharField(max_length=50, validators=[validators.MinLengthValidator(2)])
    image = models.FileField(upload_to='static/images/uploads/gallery')
    uploaded_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Stories(models.Model):
    name = models.CharField(max_length=50, validators=[validators.MinLengthValidator(2)])
    image = models.FileField(upload_to='static/images/uploads/stories')
    detail = models.TextField(max_length=2000, validators=[validators.MinLengthValidator(50)])
    uploaded_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    options = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'))
    firstname = models.CharField(max_length=100, validators=[validators.MinLengthValidator(2)])
    lastname = models.CharField(max_length=100, validators=[validators.MinLengthValidator(2)])
    email = models.EmailField(validators=[validators.EmailValidator])
    phone = models.CharField(max_length=10, validators=[validators.MinLengthValidator(10)])
    date = models.DateField(max_length=20)
    time = models.TimeField(max_length=10)
    person = models.CharField(max_length=2, choices=options)
    completion = models.BooleanField(default=False)
    reserved_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Catering(models.Model):
    options1 = (('Weddings', 'Weddings'), ('Birthday Parties', 'Birthday Parties'), ('Anniversary Parties', 'Anniversary Parties'), ('Business Meetings', 'Business Meetings'),
                ('Conferences', 'Conferences'), ('Luncheons', 'Luncheons'), ('Holiday Gatherings', 'Holiday Gatherings'), ('Other', 'Other'))
    options2 = (('On-promise', 'On-promise'), ('Off-promise', 'Off-promise'))
    firstname = models.CharField(max_length=100, validators=[validators.MinLengthValidator(2)])
    lastname = models.CharField(max_length=100, validators=[validators.MinLengthValidator(2)])
    email = models.EmailField(validators=[validators.EmailValidator])
    phone = models.CharField(max_length=10, validators=[validators.MinLengthValidator(10)])
    date = models.DateField()
    time = models.TimeField()
    event_type = models.CharField(max_length=50, choices=options1)
    catering_type = models.CharField(max_length=50, choices=options2)
    address = models.CharField(blank=True, max_length=50, validators=[validators.MinLengthValidator(10)])
    completion = models.BooleanField(default=False)
    catering_order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Message(models.Model):
    subject = models.CharField(max_length=50, validators=[validators.MinLengthValidator(2)], null=True)
    messages = models.TextField(max_length=2000, validators=[validators.MinLengthValidator(50)], null=True)
    messaged_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name