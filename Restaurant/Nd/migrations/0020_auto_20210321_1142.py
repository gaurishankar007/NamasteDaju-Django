# Generated by Django 3.1.6 on 2021-03-21 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Nd', '0019_auto_20210321_1101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='order',
            name='lastname',
        ),
    ]
