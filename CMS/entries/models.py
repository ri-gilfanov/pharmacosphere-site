from django.conf import settings
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey
from django.db.models.signals import post_delete
from core.model_functions import del_img_at_obj_del, del_img_at_obj_change


class Category(MPTTModel):
    name = models.CharField('название', max_length=128)
    parent = TreeForeignKey('self', models.CASCADE, blank=True, db_index=True, null=True,
                            related_name='children', verbose_name='родительская категория')

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'категория публикаций'
        verbose_name_plural = 'категории публикаций'


class Abs(models.Model):
    title = models.CharField('заголовок', max_length=128)
    text = RichTextUploadingField('текст', config_name='dflt_config')
    pub_date = models.DateTimeField('время публикации', default=timezone.now)
    is_anonymously = models.BooleanField('анонимная публикация', default=False)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class Entry(Abs):
    image = models.ImageField('обложка', blank=True, upload_to='entries/pub/%Y/%m/%d/')
    category = models.ForeignKey(Category, models.CASCADE, verbose_name='категория')
    is_chosen = models.BooleanField('избранная', default=False)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, verbose_name='создатель публикации')
    company = models.ForeignKey('companies.Company', models.CASCADE, blank=True, null=True,
                                verbose_name='компания')

    def save(self, *args, **kwargs):
        del_img_at_obj_change(post_object=self)
        super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'


post_delete.connect(del_img_at_obj_del, Entry)


class EntryDraft(Abs):
    image = models.ImageField('обложка', blank=True, upload_to='entries/sug/%Y/%m/%d/')
    category = models.ForeignKey(Category, models.CASCADE, verbose_name='категория', blank=True, null=True)
    is_ready = models.BooleanField('готово для размещения', default=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, verbose_name='создатель черновика')
    company = models.ForeignKey('companies.Company', models.CASCADE, blank=True, null=True,
                                verbose_name='компания')
    entry = models.OneToOneField(Entry, models.CASCADE, blank=True, null=True,
                                 verbose_name='публикация')
    is_published = models.BooleanField('опубликовано', default=False)

    def save(self, *args, **kwargs):
        del_img_at_obj_change(post_object=self)
        super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        ordering = ('is_published', '-is_ready', 'pub_date',)
        verbose_name = 'черновик'
        verbose_name_plural = 'черновики'


post_delete.connect(del_img_at_obj_del, EntryDraft)

