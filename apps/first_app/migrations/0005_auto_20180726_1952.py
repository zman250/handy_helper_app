# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-26 19:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_auto_20180726_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_poster', to='first_app.User'),
        ),
    ]