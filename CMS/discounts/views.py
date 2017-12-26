from django.shortcuts import render
from django.utils import timezone
from core.view_functions import get_banners_and_slider
from .models import Discount
from django.db.models import Q


PAGE_TYPE = 'discounts'
SELECT_MAIN_MENU_ITEM = '/discounts/'


def view_list(request):
    context = {}
    context['select_main_menu_item'] = SELECT_MAIN_MENU_ITEM
    context['url_paginator_page'] = 'discount_list'
    context['obj_list'] = Discount.objects.filter(
        Q(end__gte=timezone.now()) | Q(end=None),
    ).select_related('company')
    get_banners_and_slider(context, PAGE_TYPE)
    return render(request, 'discounts/obj_list.html', context)
