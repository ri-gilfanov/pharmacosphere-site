# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 07:43
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('торговля', (('buy', 'куплю'), ('cell', 'продам'))), ('работа', (('resume', 'резюме'), ('vacancy', 'вакансии'))), ('аренда', (('lease', 'сдаю'), ('rent', 'сниму'))), ('other', 'разное')], default='other', max_length=16, verbose_name='категория')),
                ('title', models.CharField(max_length=128, verbose_name='заголовок')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='текст')),
                ('premium', models.DateField(blank=True, null=True, verbose_name='дата завершения премиум-статуса')),
            ],
            options={
                'verbose_name': 'объявление',
                'ordering': ('-premium',),
                'verbose_name_plural': 'объявления',
            },
        ),
        migrations.CreateModel(
            name='AdDraft',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='отредактировано')),
                ('is_ready', models.BooleanField(default=True, verbose_name='готово для размещения')),
                ('is_published', models.BooleanField(default=False, verbose_name='опубликовано')),
                ('category', models.CharField(choices=[('торговля', (('buy', 'куплю'), ('cell', 'продам'))), ('работа', (('resume', 'резюме'), ('vacancy', 'вакансии'))), ('аренда', (('lease', 'сдаю'), ('rent', 'сниму'))), ('other', 'разное')], default='other', max_length=16, verbose_name='категория')),
                ('title', models.CharField(max_length=128, verbose_name='заголовок')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='текст')),
                ('ad', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ad_draft', to='ads.Ad', verbose_name='объявление')),
            ],
            options={
                'verbose_name': 'черновик',
                'ordering': ('is_published', 'last_modified'),
                'verbose_name_plural': 'черновики',
            },
        ),
    ]
