from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render
from core.view_functions import get_banners_and_slider, get_extend_paginator
from .models import User, UserDraft
from .forms import UserForm, UserDraftForm
from django.template.context_processors import csrf
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


PAGE_TYPE = 'persons'
SELECT_MAIN_MENU_ITEM = '/persons/'


def view_list(request, page_number):
    context = {}
    context['select_main_menu_item'] = SELECT_MAIN_MENU_ITEM
    context['url_paginator_page'] = 'user_list'
    obj_list = User.objects.all().only('id', 'username', 'last_name', 'first_name', 'patronymic', 'image')
    get_extend_paginator(context, obj_list, page_number, 10)
    get_banners_and_slider(context, PAGE_TYPE)
    return render(request, 'users/obj_list.html', context)


def view_obj(request, pk):
    context = {}
    context['select_main_menu_item'] = SELECT_MAIN_MENU_ITEM
    context['select_profile_item'] = 'profile'
    context['obj'] = User.objects.get(pk=pk)
    get_banners_and_slider(context, PAGE_TYPE)
    return render(request, 'users/obj.html', context)


def view_obj_entries(request, pk, page_number):
    context = {}
    context['select_main_menu_item'] = SELECT_MAIN_MENU_ITEM
    context['select_profile_item'] = 'entries'
    context['url_paginator_page'] = 'url_user_entries'
    context['obj'] = User.objects.get(pk=pk)
    obj_list = context['obj'].entry_set.filter(is_anonymously=False)
    get_extend_paginator(context, obj_list, page_number, 10)
    get_banners_and_slider(context, PAGE_TYPE)
    return render(request, 'users/obj_entries.html', context)


def view_obj_ads(request, pk, page_number):
    context = {}
    context['select_main_menu_item'] = SELECT_MAIN_MENU_ITEM
    context['select_profile_item'] = 'ads'
    context['url_paginator_page'] = 'url_user_ads'
    context['obj'] = User.objects.get(pk=pk)
    obj_list = context['obj'].ad_set.filter(company=None).select_related('creator', 'company')
    get_extend_paginator(context, obj_list, page_number, 10)
    get_banners_and_slider(context, PAGE_TYPE)
    return render(request, 'users/obj_ads.html', context)


@login_required
def view_profile_edit(request):
    user, req_FILES, req_POST = request.user, request.FILES, request.POST
    context = {}
    context.update(csrf(request))
    context['select_main_menu_item'] = SELECT_MAIN_MENU_ITEM
    context['select_profile_item'] = 'profile'
    get_banners_and_slider(context, PAGE_TYPE)
    if user.is_staff:
        if req_POST:
            context['form'] = UserForm(req_POST, req_FILES, instance=user)
            if context['form'].is_valid():
                context['form'].save()
        else:
            context['form'] = UserForm(instance=user)
        context['obj'] = user
        return render(request, 'users/obj_edit.html', context)
    else:
        draft, created = UserDraft.objects.get_or_create(
            user=user,
            defaults={
                'last_name': user.last_name,
                'first_name': user.first_name,
                'patronymic': user.patronymic,
                'text': user.text,
                'birth_date': user.birth_date,
                'image': user.image,
            },
        )
        if created:
            pass  # прописать копирование аватарки из user в draft
        if req_POST:
            draft.is_published = False
            context['form'] = UserDraftForm(req_POST, req_FILES, instance=draft)
            if context['form'].is_valid():
                context['form'].save()
        else:
            context['form'] = UserDraftForm(instance=draft)
        context['obj'] = draft
        return render(request, 'users/obj_edit.html', context)
