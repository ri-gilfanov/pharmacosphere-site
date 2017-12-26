# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-27 04:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0005_auto_20170305_0502'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ad',
            options={'ordering': ('-premium', '-pk'), 'verbose_name': 'объявление', 'verbose_name_plural': 'объявления'},
        ),
        migrations.AddField(
            model_name='ad',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='время публикации'),
        ),
        migrations.AddField(
            model_name='addraft',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='время публикации'),
        ),
    ]
