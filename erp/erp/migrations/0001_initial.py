# Generated by Django 2.1.3 on 2018-11-16 03:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('cep', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^(\\d\\d\\.\\d\\d\\d-\\d\\d\\d|\\d\\d\\d\\d\\d-\\d\\d\\d|\\d\\d\\d\\d\\d\\d\\d\\d)$'), django.core.validators.MinLengthValidator(8), django.core.validators.MaxLengthValidator(10)])),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=20)),
                ('public_place', models.CharField(max_length=100)),
                ('neighborhood', models.CharField(max_length=100)),
            ],
        ),
    ]
