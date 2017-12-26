from django.contrib import admin
from .models import Slide, Slider
from django import forms


class SliderAdminForm(forms.ModelForm):
    # Переопределение формы редактирования слайдера с ограничением выбора страниц показа
    def __init__(self, *args, **kwargs):
        super(SliderAdminForm, self).__init__(*args, **kwargs)
        sliders = Slider.objects.exclude(display_pages='не выбраны')
        selected_choices = sliders.values_list('display_pages', flat=True)
        self.fields['display_pages'].choices = [
            choice for choice in self.fields['display_pages'].choices if choice[0] not in selected_choices
            or (
                'instance' in kwargs
                and 'display_pages' in dir(kwargs['instance'])
                and choice[0] == kwargs['instance'].display_pages
            )
        ]


class SlideInline(admin.TabularInline):
    model = Slide
    extra = 1
    fields = ('image', 'background_color', 'url_link', 'new_tab', 'position',)


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    form = SliderAdminForm
    inlines = (SlideInline,)
