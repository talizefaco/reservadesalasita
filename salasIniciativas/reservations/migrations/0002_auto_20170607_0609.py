# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salacasd',
            name='comecoReserva',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='salacasd',
            name='terminoReserva',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='salacasdinho',
            name='comecoReserva',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='salacasdinho',
            name='terminoReserva',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='salacasdvest',
            name='comecoReserva',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='salacasdvest',
            name='terminoReserva',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='saladepcult',
            name='comecoReserva',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='saladepcult',
            name='terminoReserva',
            field=models.CharField(max_length=64),
        ),
    ]
