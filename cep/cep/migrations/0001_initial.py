# Generated by Django 2.1.3 on 2018-11-15 14:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('acronym', models.CharField(max_length=2, unique=True, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.RegexValidator('^[A-Z]{2}$', message='Ensure all letter be capitalized.')])),
            ],
        ),
    ]