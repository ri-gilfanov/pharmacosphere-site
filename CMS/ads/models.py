from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db.models.signals import post_save
from django.utils import timezone


CATEGORY_CHOICES = (
    ('торговля', (('buy', 'куплю'), ('cell', 'продам'))),
    ('работа', (('resume', 'резюме'), ('vacancy', 'вакансии'))),
    ('аренда', (('lease', 'сдаю'), ('rent', 'сниму'))),
    ('other', 'разное'),
)


class Abs(models.Model):
    category = models.CharField('категория', choices=CATEGORY_CHOICES, default='other',
                                max_length=16)
    title = models.CharField('заголовок', max_length=128)
    text = RichTextUploadingField('текст', config_name='dflt_config')
    pub_date = models.DateTimeField('время публикации', default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class Ad(Abs):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, verbose_name='создатель объявления')
    company = models.ForeignKey('companies.Company', models.CASCADE, blank=True, null=True,
                                verbose_name='компания')
    premium = models.DateField('дата завершения премиум-статуса', blank=True, null=True)

    class Meta:
        ordering = ('-premium', '-pk',)
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'


class AdDraft(Abs):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, verbose_name='создатель черновика')
    company = models.ForeignKey('companies.Company', models.CASCADE, blank=True, null=True, verbose_name='компания')
    ad = models.OneToOneField(Ad, models.CASCADE, blank=True, null=True, related_name='ad_draft', verbose_name='объявление')
    is_ready = models.BooleanField('готово для размещения', default=True)
    is_published = models.BooleanField('опубликовано', default=False)

    class Meta:
        ordering = ('is_published', '-is_ready', 'pk',)
        verbose_name = 'черновик'
        verbose_name_plural = 'черновики'
