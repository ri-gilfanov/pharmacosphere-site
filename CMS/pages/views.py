from django.contrib import auth, messages
from django.http import Http404
from django.shortcuts import redirect, render
from django.template.context_processors import csrf
from entries.models import Entry
from discounts.models import Discount
from ads.models import Ad
from core.view_functions import get_banners_and_slider
from .models import CustomPage
from django.db.models import Q
from django.utils import timezone


def custom_page(request, pk):
    context = {}
    obj = CustomPage.objects.get(pk=pk)
    context['obj'] = obj
    context['select_main_menu_item'] = '/page_%i/' % obj.get_root().pk
    get_banners_and_slider(context, 'custom')
    
    if obj.show_tree == 'full':
        context['descendants'] = obj.get_descendants()
    elif obj.show_tree == 'l3':
        context['descendants'] = obj.get_descendants().filter(level__lte=3)
    elif obj.show_tree == 'l2':
        context['descendants'] = obj.get_descendants().filter(level__lte=2)
    elif obj.show_tree == 'l1':
        context['descendants'] = obj.get_children()
    elif obj.show_tree == 'pv':
        context['obj_list'] = obj.get_children()
    return render(request, 'pages/custom_pages.html', context)


def main_page(request):
    context = {}
    context['select_main_menu_item'] = '/'

    tmp = Entry.objects.filter()[:10]
    tmp = tmp.values('pk', 'title', 'pub_date')
    context['entries_list_widget'] = tmp

    tmp = Discount.objects.filter(
        Q(end__gte=timezone.now()) | Q(end=None),
    )[:5]
    tmp = tmp.values('pk', 'start', 'end', 'company__name')
    context['discounts_list_widget'] = tmp

    tmp = Ad.objects.filter()[:5]
    tmp = tmp.values('pk', 'title', 'pub_date')
    context['ads_list_widget'] = tmp

    tmp = Entry.objects.filter(is_chosen=True).prefetch_related(
        'category',
        'creator',
        'company',
    )
    context['chosen_entries'] = tmp

    get_banners_and_slider(context, page_type='main')
    return render(request, 'pages/main_page.html', context)


def not_found(request):
    context = {}
    return render(request, 'pages/404.html', context, status=404)


def log_in(request):
    context = {}
    context['select_main_menu_item'] = '/'
    context.update(csrf(request))
    context['auth_form'] = auth.forms.AuthenticationForm()
    req_POST = request.POST
    if req_POST and 'username' in req_POST and 'password' in req_POST:
        user = auth.authenticate(username=req_POST['username'], password=req_POST['password'])
        if user:
            auth.login(request, user)
        else:
            messages.warning(request, '<p>Ошибка. Неверное имя пользователя или пароль.</p>')
    if not request.user.is_authenticated():
        return render(request, 'pages/log_in.html', context)
    else:
        return redirect('/')


def log_out(request):
    auth.logout(request)
    if 'HTTP_REFERER' in request.META:
        return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect('/')
