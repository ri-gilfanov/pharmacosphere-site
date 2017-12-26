from django.db import models
from django.db.models.signals import post_delete
from core.model_functions import del_img_at_obj_del, del_img_at_obj_change
from core.model_mixins import DisplayPagesMixin


class Slider(DisplayPagesMixin):
    name = models.CharField('название слайдера', max_length=128, unique=True)
    company = models.ForeignKey('companies.Company', models.CASCADE, verbose_name='компания')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'слайдер'
        verbose_name_plural = 'слайдеры'


class Slide(models.Model):
    image = models.ImageField('изображение', upload_to='slides/%Y/%m/%d/')
    background_color = models.CharField('Цвет фона', default='rgba(0, 0, 0, 1.0)', max_length=25)
    url_link = models.CharField('ссылка', blank=True, max_length=128)
    new_tab = models.BooleanField('открывать ссылку в новой вкладке', default=True)
    position = models.SmallIntegerField('позиция', blank=True, null=True)
    slider = models.ForeignKey(Slider, models.CASCADE, related_name='slides')

    def save(self, *args, **kwargs):
        del_img_at_obj_change(post_object=self)
        super(Slide, self).save(*args, **kwargs)

    class Meta:
        ordering = ('position', 'pk',)
        verbose_name = 'слайд'
        verbose_name_plural = 'слайды'


post_delete.connect(del_img_at_obj_del, Slide)
