from django.db import models
from django.db.models.signals import post_delete
from core.model_functions import del_img_at_obj_del, del_img_at_obj_change
from core.model_mixins import DisplayPagesMixin


class Abs(DisplayPagesMixin):
    name = models.CharField('наименование баннера', max_length=128)
    code = models.TextField('код баннера')
    start = models.DateField(blank=True, null=True, verbose_name='начало показа')
    end = models.DateField(blank=True, null=True, verbose_name='завершение показа')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class TopBanner(Abs):
    image = models.ImageField('изображение', blank=True, upload_to='banners/top/%Y/%m/%d/')
    company = models.ForeignKey('companies.Company', models.CASCADE, verbose_name='компания')

    def save(self, *args, **kwargs):
        del_img_at_obj_change(post_object=self)
        super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'верхний баннер'
        verbose_name_plural = 'верхние баннеры'


post_delete.connect(del_img_at_obj_del, TopBanner)


class SideBanner(Abs):
    image = models.ImageField('изображение', blank=True, upload_to='banners/side/%Y/%m/%d/')
    company = models.ForeignKey('companies.Company', models.CASCADE, verbose_name='компания')
    right_banner = models.OneToOneField('self', models.SET_NULL, blank=True, null=True,
                                        related_name='left_banner', verbose_name='правый баннер')

    def save(self, *args, **kwargs):
        del_img_at_obj_change(post_object=self)
        super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'боковой баннер'
        verbose_name_plural = 'боковые баннеры'


post_delete.connect(del_img_at_obj_del, SideBanner)
