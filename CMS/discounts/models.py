from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Discount(models.Model):
    company = models.ForeignKey('companies.Company', models.CASCADE, verbose_name='компания')
    start = models.DateField('начало акции')
    end = models.DateField('завершение акции')
    premium = models.DateField('дата завершения премиум-статуса', blank=True, null=True)
    text = RichTextUploadingField('текст', config_name='dflt_config')

    def __str__(self):
        company = self.company
        start = self.start
        end = self.end
        if company and start and end:
            return '%s (%s — %s)' % (company, start, end)
        else:
            return 'Неизвестная акция #%i' % (self.pk)

    class Meta:
        ordering = ('-premium', '-start',)
        verbose_name = 'акция'
        verbose_name_plural = 'акции'
