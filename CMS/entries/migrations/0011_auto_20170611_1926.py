# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-11 16:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0010_auto_20170611_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='category',
        ),
        migrations.RemoveField(
            model_name='entrydraft',
            name='category',
        ),
    ]
