from django.conf.urls import url
from .views import (
    view_list,
    view_obj,
    view_obj_entries,
    view_obj_discounts,
    view_obj_ads,
    view_obj_contacts,
)


urlpatterns = [
    url(r'^(?:page_(?P<page_number>\d+)/)?$', view_list, name='company_list'),
    url(r'^(?P<pk>\d+)/$', view_obj, name='url_company_obj'),
    url(r'^(?P<pk>\d+)/entries/(?:page_(?P<page_number>\d+)/)?$', view_obj_entries, name='url_company_entries'),
    url(r'^(?P<pk>\d+)/discounts/(?:page_(?P<page_number>\d+)/)?$', view_obj_discounts, name='url_company_discounts'),
    url(r'^(?P<pk>\d+)/ads/(?:page_(?P<page_number>\d+)/)?$', view_obj_ads, name='url_company_ads'),
    url(r'^(?P<pk>\d+)/contacts/$', view_obj_contacts, name='url_company_contacts'),
]
