# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-09 03:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorinfo', '0002_auto_20181120_1003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctorprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='doctorprofile',
            name='age',
            field=models.CharField(default=1, max_length=10),
        ),
        migrations.AddField(
            model_name='doctorprofile',
            name='experience',
            field=models.CharField(default=1, max_length=100),
        ),
        migrations.AddField(
            model_name='doctorprofile',
            name='gender',
            field=models.CharField(choices=[('m', 'Male'), ('f', 'Female')], default=1, max_length=10),
        ),
        migrations.AddField(
            model_name='doctorprofile',
            name='image',
            field=models.ImageField(default=1, upload_to='media/'),
        ),
    ]
