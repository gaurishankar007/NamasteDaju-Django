# Generated by Django 3.1.6 on 2021-03-14 08:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nd', '0010_auto_20210314_1323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catering',
            name='complition',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='complition',
        ),
        migrations.AddField(
            model_name='catering',
            name='completion',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='completion',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='catering',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
        migrations.AlterField(
            model_name='catering',
            name='email',
            field=models.EmailField(max_length=254, null=True, validators=[django.core.validators.EmailValidator]),
        ),
    ]
