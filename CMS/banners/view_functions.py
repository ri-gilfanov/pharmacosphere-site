from .models import TopBanner, SideBanner
from django.utils import timezone
from random import randint
from django.db.models import Q


def get_banners(context, page_type=None):
    def date_exclude(query_set):
        return query_set.filter(
            Q(start__lte=timezone.now()) | Q(start=None),
            Q(end__gte=timezone.now()) | Q(end=None),
        )

    display_pages_A = {'display_pages__in': ['main', 'all']}
    display_pages_B = {'display_pages__in': [page_type, 'not_main', 'all']}
    left_banner = None

    if 'top_banner' not in context:
        if page_type == 'main':
            top_bnrs_list = TopBanner.objects.filter(**display_pages_A)
        else:
            top_bnrs_list = TopBanner.objects.filter(**display_pages_B)
        top_bnrs_list = date_exclude(top_bnrs_list)
        count = len(top_bnrs_list)  # -1 запрос в сравнении с .count()
        if count:
            top_banner = top_bnrs_list[randint(0, count - 1)]
            context['top_banner'] = top_banner

    if 'left_banner' not in context:
        if page_type == 'main':
            left_bnrs_list = SideBanner.objects.filter(**display_pages_A)
        else:
            left_bnrs_list = SideBanner.objects.filter(**display_pages_B)
        left_bnrs_list = date_exclude(left_bnrs_list)
        count = len(left_bnrs_list)
        if count:
            left_banner = left_bnrs_list[randint(0, count - 1)]
            context['left_banner'] = left_banner

    display_pages_A['right_banner'] = None
    display_pages_B['right_banner'] = None
    if 'right_banner' not in context:
        if page_type == 'main':
            right_bnrs_list = SideBanner.objects.filter(**display_pages_A)
        else:
            right_bnrs_list = SideBanner.objects.filter(**display_pages_B)
        right_bnrs_list = date_exclude(right_bnrs_list)
        if left_banner:
            if left_banner.right_banner:
                context['right_banner'] = left_banner.right_banner
            else:
                right_bnrs_list = right_bnrs_list.exclude(pk=left_banner.pk)
        count = len(right_bnrs_list)
        if 'right_banner' not in context and count:
            right_banner = right_bnrs_list[randint(0, count - 1)]
            context['right_banner'] = right_banner
