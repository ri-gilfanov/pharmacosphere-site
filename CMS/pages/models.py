from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey


class CustomPage(MPTTModel):
    title = models.CharField('заголовок', max_length=384)
    text = RichTextUploadingField('текст', blank=True, config_name='dflt_config')
    parent = TreeForeignKey('self', models.CASCADE, blank=True, db_index=True, null=True,
                            related_name='children', verbose_name='родительская страница')
    show_tree = models.CharField(
        'показывать вложенные страницы',
        choices=(
            ('full', 'полное древо'),
            ('l3', 'на три уровня'),
            ('l2', 'на два уровня'),
            ('l1', 'на один уровень'),
            ('pv', 'с кратким содержание'),
            ('none', 'не показывать'),
        ),
        default='full',
        max_length=8,
    )

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        verbose_name = 'страница'
        verbose_name_plural = 'страницы'
