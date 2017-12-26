from django.shortcuts import render
from core.view_functions import get_banners_and_slider, get_extend_paginator
from .models import Company


PAGE_TYPE = 'companies'
SELECT_MAIN_MENU_ITEM = '/companies/'


def view_list(request, page_number):
    context = {}
    context['select_main_menu_item'] = SELECT_MAIN_MENU_ITEM
    context['url_paginator_page'] = 'company_list'
    obj_list = Company.objects.filter() \
        .only('id', 'name', 'image')
    get_extend_paginator(context, obj_list, page_number, 20)
    get_banners_and_slider(context, PAGE_TYPE)
    return render(request, 'companies/obj_list.html', context)


def view_obj(request, pk):
    context = {}
    context['select_main_menu_item'] = SELECT_MAIN_MENU_ITEM
    context['select_profile_item'] = 'profile'
    context['obj'] = Company.objects.get(pk=pk)
    get_banners_and_slider(context, PAGE_TYPE)
    return render(request, 'companies/obj.html', context)


def view_obj_entries(request, pk, page_number):
    context = {}
    context['select_main_menu_item'] = SELECT_MAIN_MENU_ITEM
    context['select_profile_item'] = 'entries'
    context['url_paginator_page'] = 'url_company_entries'
    context['obj'] = Company.objects.get(pk=pk)
    print(dir(context['obj']))
    obj_list = context['obj'].entry_set.all()
    get_extend_paginator(context, obj_list, page_number, 10)
    get_banners_and_slider(context, PAGE_TYPE)
    return render(request, 'companies/obj_entries.html', context)


def view_obj_discounts(request, pk, page_number):
    context = {}
    context['select_main_menu_item'] = SELECT_MAIN_MENU_ITEM
    context['select_profile_item'] = 'discounts'
    context['url_paginator_page'] = 'url_company_discounts'
    context['obj'] = Company.objects.get(pk=pk)
    context['obj_list'] = context['obj'].discount_set.all()
    get_banners_and_slider(context, PAGE_TYPE)
    return render(request, 'companies/obj_discounts.html', context)


def view_obj_ads(request, pk, page_number):
    context = {}
    context['select_main_menu_item'] = SELECT_MAIN_MENU_ITEM
    context['select_profile_item'] = 'ads'
    context['url_paginator_page'] = 'url_company_ads'
    context['obj'] = Company.objects.get(pk=pk)
    obj_list = context['obj'].ad_set.all().select_related('creator', 'company')
    get_extend_paginator(context, obj_list, page_number, 10)
    get_banners_and_slider(context, PAGE_TYPE)
    return render(request, 'companies/obj_ads.html', context)


def view_obj_contacts(request, pk):
    context = {}
    context['obj'] = Company.objects.get(pk=pk)
    context['select_main_menu_item'] = SELECT_MAIN_MENU_ITEM
    context['select_profile_item'] = 'contacts'
    get_banners_and_slider(context, PAGE_TYPE)
    return render(request, 'companies/obj_contacts.html', context)
