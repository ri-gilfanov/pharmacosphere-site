# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 05:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0005_auto_20170304_0737'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entrydraft',
            options={'ordering': ('is_published', '-is_ready', 'pub_date'), 'verbose_name': 'черновик', 'verbose_name_plural': 'черновики'},
        ),
    ]
