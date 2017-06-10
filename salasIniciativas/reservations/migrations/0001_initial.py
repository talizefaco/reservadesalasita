# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 03:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='salaCasd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comecoReserva', models.DateTimeField()),
                ('terminoReserva', models.DateTimeField()),
                ('donoReserva', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='salaCasdinho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comecoReserva', models.DateTimeField()),
                ('terminoReserva', models.DateTimeField()),
                ('donoReserva', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='salaCasdVest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comecoReserva', models.DateTimeField()),
                ('terminoReserva', models.DateTimeField()),
                ('donoReserva', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='salaDepCult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comecoReserva', models.DateTimeField()),
                ('terminoReserva', models.DateTimeField()),
                ('donoReserva', models.CharField(max_length=64)),
            ],
        ),
    ]