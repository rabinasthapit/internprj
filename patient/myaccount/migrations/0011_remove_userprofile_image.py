# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-10 05:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myaccount', '0010_auto_20190209_1953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='image',
        ),
    ]