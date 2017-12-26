from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from django.template.context_processors import csrf
from core.view_functions import get_banners_and_slider, get_extend_paginator
from .forms import AdForm, AdDraftForm, PublishedAdDraftForm
from .models import Ad, AdDraft


PAGE_TYPE = 'ads'
SELECT_MAIN_MENU_ITEM = '/ads/'


def view_list(request, page_number):
    context = {}
    context['select_main_menu_item'] = SELECT_MAIN_MENU_ITEM
    context['url_paginator_page'] = 'url_ad_list'
    obj_list = Ad.objects.all().select_related('creator', 'company')
    get_extend_paginator(context, obj_list, page_number, 10)
    get_banners_and_slider(context, PAGE_TYPE)
    return render(request, 'ads/obj_list.html', context)


@login_required
def view_draft_list(request, page_number):
    context = {}
    context['select_main_menu_item'] = SELECT_MAIN_MENU_ITEM
    context['url_paginator_page'] = 'url_ad_draft_list'
    obj_list = AdDraft.objects.filter(creator=request.user, is_published=False)
    get_extend_paginator(context, obj_list, page_number, 10)
    get_banners_and_slider(context, PAGE_TYPE)
    return render(request, 'ads/draft_list.html', context)


def view_obj(request, pk):
    context = {}
    context['obj'] = Ad.objects.get(pk=pk)
    context['select_main_menu_item'] = SELECT_MAIN_MENU_ITEM
    get_banners_and_slider(context, PAGE_TYPE)
    return render(request, 'ads/obj_show_page.html', context)


@login_required
def view_obj_add(request):
    user = request.user
    if user.is_staff:
        context = {}
        context.update(csrf(request))
        context['select_main_menu_item'] = SELECT_MAIN_MENU_ITEM
        req_POST = request.POST
        if req_POST:
            ad = Ad(creator=user)
            context['form'] = AdForm(req_POST, instance=ad)
            if context['form'].is_valid():
                context['form'].save()
                return redirect(reverse('url_ad_list'))
        else:
            ad = Ad(creator=user)
            context['form'] = AdForm(instance=ad)
        get_banners_and_slider(context, PAGE_TYPE)
        return render(request, 'ads/obj_add.html', context)
    return redirect(reverse('url_ad_list'))


@login_required
def view_draft_add(request):
    context = {}
    context.update(csrf(request))
    context['select_main_menu_item'] = SELECT_MAIN_MENU_ITEM
    user = request.user
    req_POST = request.POST
    if req_POST:
        draft = AdDraft(creator=user)
        context['form'] = AdDraftForm(req_POST, instance=draft)
        if context['form'].is_valid():
            context['form'].save()
            return redirect(reverse('url_ad_draft_list'))
    else:
        draft = AdDraft(creator=user)
        context['form'] = AdDraftForm(instance=draft)
    get_banners_and_slider(context, PAGE_TYPE)
    return render(request, 'ads/draft_add.html', context)


@login_required
def view_obj_edit(request, pk):
    user = request.user
    ad = Ad.objects.get(pk=pk)
    if user.is_staff or user.pk == ad.creator.pk:
        if user.is_staff:
            context = {}
            context.update(csrf(request))
            context['select_main_menu_item'] = SELECT_MAIN_MENU_ITEM
            req_POST = request.POST
            if req_POST:
                context['form'] = AdForm(req_POST, instance=ad)
                if context['form'].is_valid():
                    context['form'].save()
                    return redirect(reverse('url_ad_obj', args=pk))
            else:
                context['form'] = AdForm(instance=ad)
            context['obj'] = ad
            get_banners_and_slider(context, PAGE_TYPE)
            return render(request, 'ads/obj_edit.html', context)
        else:
            draft, created = AdDraft.objects.get_or_create(
                ad=ad,
                defaults={
                    'category': ad.category,
                    'company': ad.company,
                    'creator': ad.creator,
                    'text': ad.text,
                    'title': ad.title,
                },
            )
            return redirect(reverse('url_ad_draft_edit', args=[draft.pk]))
    return redirect(reverse('url_ad_obj', args=pk))


@login_required
def view_draft_edit(request, pk):
    user = request.user
    draft = AdDraft.objects.get(pk=pk)
    if user.pk == draft.creator.pk:
        context = {}
        context.update(csrf(request))
        context['select_main_menu_item'] = SELECT_MAIN_MENU_ITEM
        req_POST = request.POST
        if draft.entry:
            Form = PublishedAdDraftForm
        else:
            Form = AdDraftForm
        if req_POST:
            draft.is_published = False
            context['form'] = Form(req_POST, instance=draft)
            if context['form'].is_valid():
                context['form'].save()
                return redirect(reverse('url_ad_draft_list'))
        else:
            context['form'] = Form(instance=draft)
        context['obj'] = draft
        get_banners_and_slider(context, PAGE_TYPE)
        return render(request, 'ads/draft_edit.html', context)
    return redirect(reverse('url_ad_draft_list'))
