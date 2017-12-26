from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from django.template.context_processors import csrf
from django.utils import timezone
from core.view_functions import get_banners_and_slider, get_extend_paginator
from .forms import EntryForm, EntryDraftForm, PublishedEntryDraftForm
from .models import Entry, EntryDraft
from .filters import EntryFilter


PAGE_TYPE = 'entries'
SELECT_MAIN_MENU_ITEM = '/entries/'


def view_list(request, page_number):
    context = {}
    context['select_main_menu_item'] = SELECT_MAIN_MENU_ITEM
    context['url_paginator_page'] = 'entry_list'
    filter_ = EntryFilter(request.GET, queryset=Entry.objects.filter(pub_date__lte=timezone.now()))
    obj_list = filter_.qs
    context['filter'] = filter_
    context['GET_parameters'] = '?%s' % (request.GET.urlencode())
    get_extend_paginator(context, obj_list, page_number, 10)
    get_banners_and_slider(context, PAGE_TYPE)
    return render(request, 'entries/obj_list.html', context)


@login_required
def view_draft_list(request, page_number):
    context = {}
    context['select_main_menu_item'] = SELECT_MAIN_MENU_ITEM
    context['url_paginator_page'] = 'url_entry_draft_list'
    obj_list = EntryDraft.objects.filter(creator=request.user, is_published=False)
    get_extend_paginator(context, obj_list, page_number, 10)
    get_banners_and_slider(context, PAGE_TYPE)
    return render(request, 'entries/draft_list.html', context)


def view_obj(request, pk):
    context = {}
    context['obj'] = Entry.objects.get(pk=pk)
    context['select_main_menu_item'] = SELECT_MAIN_MENU_ITEM
    get_banners_and_slider(context, PAGE_TYPE)
    return render(request, 'entries/obj_show_page.html', context)


@login_required
def view_obj_add(request):
    user = request.user
    if user.is_staff:
        context = {}
        context.update(csrf(request))
        context['select_main_menu_item'] = SELECT_MAIN_MENU_ITEM
        req_POST = request.POST
        if req_POST:
            entry = Entry(creator=user)
            context['form'] = EntryForm(req_POST, instance=entry)
            if context['form'].is_valid():
                context['form'].save()
                return redirect(reverse('entry_list'))
        else:
            entry = Entry(creator=user, pub_date=timezone.now())
            context['form'] = EntryForm(instance=entry)
        get_banners_and_slider(context, PAGE_TYPE)
        return render(request, 'entries/obj_add.html', context)
    return redirect(reverse('entry_list'))


@login_required
def view_draft_add(request):
    context = {}
    context.update(csrf(request))
    context['select_main_menu_item'] = SELECT_MAIN_MENU_ITEM
    user = request.user
    req_POST = request.POST
    if req_POST:
        draft = EntryDraft(creator=user)
        context['form'] = EntryDraftForm(req_POST, instance=draft)
        if context['form'].is_valid():
            context['form'].save()
            return redirect(reverse('url_entry_draft_list'))
    else:
        draft = EntryDraft(creator=user)
        context['form'] = EntryDraftForm(instance=draft)
    get_banners_and_slider(context, PAGE_TYPE)
    return render(request, 'entries/draft_add.html', context)


@login_required
def view_obj_edit(request, pk):
    user = request.user
    entry = Entry.objects.get(pk=pk)
    if user.is_staff or user.pk == entry.creator.pk:
        if user.is_staff:
            context = {}
            context.update(csrf(request))
            context['select_main_menu_item'] = SELECT_MAIN_MENU_ITEM
            req_POST = request.POST
            if req_POST:
                context['form'] = EntryForm(req_POST, instance=entry)
                if context['form'].is_valid():
                    context['form'].save()
                    return redirect(reverse('url_entry_obj', args=pk))
            else:
                context['form'] = EntryForm(instance=entry)
            context['obj'] = entry
            get_banners_and_slider(context, PAGE_TYPE)
            return render(request, 'entries/obj_edit.html', context)
        else:
            draft, created = EntryDraft.objects.get_or_create(
                entry=entry,
                defaults={
                    'category': entry.category,
                    'company': entry.company,
                    'creator': entry.creator,
                    'pub_date': entry.pub_date,
                    'text': entry.text,
                    'title': entry.title,
                },
            )
            return redirect(reverse('url_entry_draft_edit', args=[draft.pk]))
    return redirect(reverse('url_entry_obj', args=pk))


@login_required
def view_draft_edit(request, pk):
    user = request.user
    draft = EntryDraft.objects.get(pk=pk)
    if user.pk == draft.creator.pk:
        context = {}
        context.update(csrf(request))
        context['select_main_menu_item'] = SELECT_MAIN_MENU_ITEM
        req_POST = request.POST
        if draft.entry:
            Form = PublishedEntryDraftForm
        else:
            Form = EntryDraftForm
        if req_POST:
            draft.is_published = False
            context['form'] = Form(req_POST, instance=draft)
            if context['form'].is_valid():
                context['form'].save()
                return redirect(reverse('url_entry_draft_list'))
        else:
            context['form'] = Form(instance=draft)
        context['obj'] = draft
        get_banners_and_slider(context, PAGE_TYPE)
        return render(request, 'entries/draft_edit.html', context)
    return redirect(reverse('url_entry_draft_list'))
