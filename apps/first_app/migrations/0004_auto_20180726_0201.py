# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-26 02:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_auto_20180725_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='travel_end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='travel_start_date',
            field=models.DateField(),
        ),
    ]
