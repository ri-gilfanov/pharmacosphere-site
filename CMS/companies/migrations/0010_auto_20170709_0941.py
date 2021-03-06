# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-09 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0009_auto_20170709_0912'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pubemail',
            options={'ordering': ('position',), 'verbose_name': 'электронная почта', 'verbose_name_plural': 'электронная почта'},
        ),
        migrations.AlterModelOptions(
            name='sugemail',
            options={'ordering': ('position',), 'verbose_name': 'электронная почта', 'verbose_name_plural': 'электронная почта'},
        ),
        migrations.AlterField(
            model_name='pubemail',
            name='description',
            field=models.CharField(blank=True, max_length=128, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='pubphone',
            name='description',
            field=models.CharField(blank=True, max_length=128, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='sugemail',
            name='description',
            field=models.CharField(blank=True, max_length=128, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='sugphone',
            name='description',
            field=models.CharField(blank=True, max_length=128, verbose_name='описание'),
        ),
    ]
