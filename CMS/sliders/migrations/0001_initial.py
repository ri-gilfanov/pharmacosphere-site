# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 07:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='slides/%Y/%m/%d/', verbose_name='изображение')),
                ('background_color', models.CharField(default='rgba(0, 0, 0, 1.0)', max_length=25, verbose_name='Цвет фона')),
                ('url_link', models.CharField(blank=True, max_length=128, verbose_name='ссылка')),
                ('new_tab', models.BooleanField(default=True, verbose_name='открывать ссылку в новой вкладке')),
                ('position', models.SmallIntegerField(blank=True, null=True, verbose_name='позиция')),
            ],
            options={
                'verbose_name': 'слайд',
                'ordering': ('position', 'pk'),
                'verbose_name_plural': 'слайды',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_pages', models.CharField(choices=[('none', 'не выбраны'), ('all', 'все страницы'), ('not_main', 'кроме главной'), ('main', 'главная страница'), ('entries', 'публикации'), ('companies', 'компании'), ('persons', 'люди'), ('discounts', 'акции'), ('custom', 'произвольные страницы')], default='none', max_length=16, verbose_name='страницы показа')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='название слайдера')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.Company', verbose_name='компания')),
            ],
            options={
                'verbose_name': 'слайдер',
                'ordering': ('name',),
                'verbose_name_plural': 'слайдеры',
            },
        ),
        migrations.AddField(
            model_name='slide',
            name='slider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slides', to='sliders.Slider'),
        ),
    ]