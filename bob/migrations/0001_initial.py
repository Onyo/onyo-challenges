# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-05 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_code', models.CharField(max_length=8, unique=True)),
                ('locality', models.CharField(max_length=200)),
                ('street_number', models.CharField(blank=True, max_length=10)),
                ('country', models.CharField(blank=True, max_length=40, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
    ]