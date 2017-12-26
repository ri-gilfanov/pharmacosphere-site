from django.db import models
from django.conf import settings


class Poll(models.Model):
    question = models.CharField('вопрос', max_length=128)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True,
                                   verbose_name='пользователи')
    finish = models.DateTimeField('завершение опроса')

    class Meta:
        verbose_name = 'опрос'
        verbose_name_plural = 'опросы'


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    answer = models.CharField('ответ', max_length=128)

    class Meta:
        verbose_name = 'вариант'
        verbose_name_plural = 'варианты'
