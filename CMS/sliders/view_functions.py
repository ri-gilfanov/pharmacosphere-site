from .models import Slider


def get_slider(context, page_type=None):
    if 'slider' not in context:
        display_pages = Slider.objects.values_list('display_pages', flat=True)
        if page_type == 'main':
            if page_type in display_pages:
                context['slider'] = Slider.objects.get(display_pages=page_type)
            elif 'all' in display_pages:
                context['slider'] = Slider.objects.get(display_pages='all')
        else:
            if page_type in display_pages:
                context['slider'] = Slider.objects.get(display_pages=page_type)
            elif 'not_main' in display_pages:
                context['slider'] = Slider.objects.get(display_pages='not_main')
            elif 'all' in display_pages:
                context['slider'] = Slider.objects.get(display_pages='all')
