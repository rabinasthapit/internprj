# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-10 05:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientinfo', '0009_auto_20190205_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makeappointment',
            name='doctorname',
            field=models.CharField(default=1, max_length=100),
        ),
    ]