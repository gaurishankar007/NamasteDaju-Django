# Generated by Django 3.1.6 on 2021-03-21 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Nd', '0021_order_order_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_date',
            new_name='ordered_date',
        ),
    ]
