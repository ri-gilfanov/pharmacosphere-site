# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-15 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20170304_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custompage',
            name='title',
            field=models.CharField(max_length=256, verbose_name='заголовок'),
        ),
    ]
