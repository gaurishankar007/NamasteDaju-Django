# Generated by Django 3.1.6 on 2021-03-21 06:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nd', '0022_auto_20210321_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='foodname',
            field=models.CharField(max_length=50, null=True, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]
