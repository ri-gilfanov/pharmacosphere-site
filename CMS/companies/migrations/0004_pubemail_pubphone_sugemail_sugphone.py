# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-09 04:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_auto_20170304_0737'),
    ]

    operations = [
        migrations.CreateModel(
            name='PubEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=128, verbose_name='электронная почта')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.PubCompContact')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PubPhone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=128, verbose_name='телефон')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.PubCompContact')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SugEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=128, verbose_name='электронная почта')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.SugCompContact')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SugPhone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=128, verbose_name='телефон')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.SugCompContact')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
