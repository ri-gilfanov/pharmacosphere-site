from django.db import models


class DisplayPagesMixin(models.Model):
    display_pages = models.CharField(
        'страницы показа',
        max_length=16,
        choices=(
            ('none', 'не выбраны'),
            ('all', 'все страницы'),
            ('not_main', 'кроме главной',),
            ('main', 'главная страница'),
            ('entries', 'публикации'),
            ('companies', 'компании'),
            ('persons', 'люди'),
            ('discounts', 'акции'),
            ('custom', 'произвольные страницы'),
        ),
        default='none',
    )

    class Meta:
        abstract = True
