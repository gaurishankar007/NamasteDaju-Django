# Generated by Django 3.1.6 on 2021-03-21 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Nd', '0018_auto_20210321_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='message',
            name='lastname',
        ),
    ]
