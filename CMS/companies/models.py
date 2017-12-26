from django.conf import settings
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import post_delete
from core.model_functions import del_img_at_obj_del, del_img_at_obj_change
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Abs(models.Model):
    name = models.CharField('название', max_length=64, unique=True)
    image_50x50 = ImageSpecField(
        source='image',
        processors=[ResizeToFill(50, 50)],
        format='PNG',
        options={'quality': 60},
    )
    text = RichTextUploadingField('о компании', blank=True, config_name='dflt_config')
    web_site = models.URLField('сайт компании', blank=True, max_length=128)
    actual_address = models.CharField('фактический адрес', blank=True, max_length=128, null=True)
    legal_address = models.CharField(
        'юридический адрес',
        blank=True,
        help_text='заполняется, если отличается от фактического.',
        max_length=128,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


EMPLOYEES_NUMBER_CHOICES = (
    (0, 'не указано'),
    (1, 'от 1 до 5'),
    (2, 'от 5 до 10'),
    (3, 'от 10 до 50'),
    (4, 'от 50 до 100'),
    (5, 'от 100 до 500'),
    (6, 'от 500 до 1 000'),
    (7, 'от 1 000 до 5 000'),
    (8, 'от 5 000 до 10 000'),
    (9, 'более 10 000'),
)


class Company(Abs):
    image = models.ImageField('логотип', blank=True, upload_to='companies/pub/%Y/%m/%d/')
    employees_number = models.PositiveSmallIntegerField('число сотрудников',
                                                        choices=EMPLOYEES_NUMBER_CHOICES, default=0)
    employees = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True,
                                       related_name='employment', verbose_name='сотрудники')
    premium = models.DateField('дата завершения премиум-статуса', blank=True, null=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, verbose_name='создатель профиля')

    def save(self, *args, **kwargs):
        del_img_at_obj_change(post_object=self)
        super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        ordering = ('name',)
        verbose_name = 'профиль компании'
        verbose_name_plural = 'профили компаний'


post_delete.connect(del_img_at_obj_del, Company)


class CompanyDraft(Abs):
    image = models.ImageField('логотип', blank=True, upload_to='companies/sug/%Y/%m/%d/')
    company = models.OneToOneField(Company, models.CASCADE, blank=True, null=True,
                                   verbose_name='профиль')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, verbose_name='создатель черновика')
    last_modified = models.DateTimeField('отредактировано', auto_now=True)
    is_ready = models.BooleanField('готово для размещения', default=True)
    is_published = models.BooleanField('опубликовано', default=False)

    def save(self, *args, **kwargs):
        del_img_at_obj_change(post_object=self)
        super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        ordering = ('is_published', 'last_modified',)
        verbose_name = 'черновик профиля'
        verbose_name_plural = 'черновики профилей'


post_delete.connect(del_img_at_obj_del, CompanyDraft)


class AbsCompContact(models.Model):
    description = models.CharField('описание', blank=True, max_length=128)
    address = models.CharField('адрес', blank=True, default='', max_length=128)
    position = models.SmallIntegerField('позиция', blank=True, null=True)

    class Meta:
        abstract = True
        ordering = ('position',)
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


class PubCompContact(AbsCompContact):
    pub_company_profile = models.ForeignKey(Company, models.CASCADE, related_name='contacts')


class SugCompContact(AbsCompContact):
    sug_company_profile = models.ForeignKey(CompanyDraft, models.CASCADE, related_name='contacts')


class AbsPhone(models.Model):
    description = models.CharField('описание', blank=True, max_length=128)
    phone = models.CharField('телефон', blank=True, max_length=128)
    position = models.SmallIntegerField('позиция', blank=True, null=True)

    class Meta:
        abstract = True
        ordering = ('position',)
        verbose_name = 'телефон'
        verbose_name_plural = 'телефоны'


class PubPhone(AbsPhone):
    contact = models.ForeignKey(PubCompContact, models.CASCADE)


class SugPhone(AbsPhone):
    contact = models.ForeignKey(SugCompContact, models.CASCADE)

class AbsEmail(models.Model):
    description = models.CharField('описание', blank=True, max_length=128)
    email = models.EmailField('электронная почта', blank=True, max_length=128)
    position = models.SmallIntegerField('позиция', blank=True, null=True)

    class Meta:
        abstract = True
        ordering = ('position',)
        verbose_name = 'электронная почта'
        verbose_name_plural = 'электронная почта'


class PubEmail(AbsEmail):
    contact = models.ForeignKey(PubCompContact, models.CASCADE)


class SugEmail(AbsEmail):
    contact = models.ForeignKey(SugCompContact, models.CASCADE)
