# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-10 04:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctorinfo', '0004_doctorprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorprofile',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
