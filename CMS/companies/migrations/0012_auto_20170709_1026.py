# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-09 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0011_auto_20170709_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pubcompcontact',
            name='address',
            field=models.CharField(blank=True, default='', max_length=128, verbose_name='адрес'),
        ),
        migrations.AlterField(
            model_name='sugcompcontact',
            name='address',
            field=models.CharField(blank=True, default='', max_length=128, verbose_name='адрес'),
        ),
    ]
