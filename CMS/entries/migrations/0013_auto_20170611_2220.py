# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-11 19:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0012_auto_20170611_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='entries.Category', verbose_name='категория'),
            preserve_default=False,
        ),
    ]
