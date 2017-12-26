"""Pharmacosphere URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
import debug_toolbar
from pages.views import log_in, log_out
from django.views.decorators.cache import never_cache
handler404 = 'SntSrv.views.not_found'
from ckeditor_uploader.views import upload as ckeditor_upload, browse as ckeditor_browse
from django.contrib.auth.decorators import login_required


urlpatterns = [
    # CKEditor
    # проверка на статус персонала заменена на проверку авторизации
    url(r'^upload/', login_required(ckeditor_upload), name='ckeditor_upload'),
    url(r'^browse/', never_cache(login_required(ckeditor_browse)), name='ckeditor_browse'),

    url(r'^accounts/', include('allauth.urls')),
    url(r'^entries/', include('entries.urls')),
    url(r'^ads/', include('ads.urls')),
    url(r'^discounts/', include('discounts.urls')),
    url(r'^companies/', include('companies.urls')),
    url(r'^persons/', include('users.urls')),
    url(r'^log_in/$', log_in, name='url_log_in'),
    url(r'^log_out/$', log_out, name='url_log_out'),
    url(r'^admin/', admin.site.urls),
    url(r'^admin/login/$', log_in),
    url(r'^admin/logout/$', log_out),
    url(r'^nested_admin/', include('nested_admin.urls')),
    url(r'^', include('pages.urls')),
]



if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(url(r'^__debug__/', include(debug_toolbar.urls)))

urlpatterns.extend(
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
)


urlpatterns.extend(
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
)
