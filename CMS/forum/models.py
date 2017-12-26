from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings


class Category(models.Model):
    name = models.CharField('название категории', max_length=128)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Forum(models.Model):
    category = models.ForeignKey(Category, models.CASCADE, verbose_name='категория')
    name = models.CharField('название форума', max_length=128)

    class Meta:
        verbose_name = 'форум'
        verbose_name_plural = 'форумы'


class Topic(models.Model):
    forum = models.ForeignKey(Forum, models.CASCADE, verbose_name='форум')
    name = models.CharField('название темы', max_length=128)

    class Meta:
        verbose_name = 'тема'
        verbose_name_plural = 'темы'


class Post(models.Model):
    topic = models.ForeignKey(Topic, models.CASCADE, verbose_name='тема')
    text = RichTextUploadingField('текст сообщения', config_name='dflt_config')
    added = models.DateTimeField('добавлено', auto_now_add=True)
    edited = models.DateTimeField('отредактировно', auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.SET_NULL, null=True,
                             verbose_name='пользователь')

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
