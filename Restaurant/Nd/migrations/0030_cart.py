# Generated by Django 3.1.6 on 2021-03-24 10:51

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Nd', '0029_auto_20210323_2234'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10, null=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('foodname', models.CharField(max_length=50, null=True, validators=[django.core.validators.MinLengthValidator(2)])),
                ('quantity', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=50, null=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
