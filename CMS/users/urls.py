from django.conf.urls import url
from .views import (
    view_list,
    view_obj,
    view_profile_edit,
    view_obj_entries,
    view_obj_ads,
)


urlpatterns = [
    url(r'^(?:page_(?P<page_number>\d+)/)?$', view_list, name='user_list'),
    url(r'^(?P<pk>\d+)/$', view_obj, name='url_user_obj'),
    url(r'^edit/$', view_profile_edit, name='url_user_profile_edit'),
    url(r'^(?P<pk>\d+)/entries/(?:page_(?P<page_number>\d+)/)?$', view_obj_entries, name='url_user_entries'),
    url(r'^(?P<pk>\d+)/ads/(?:page_(?P<page_number>\d+)/)?$', view_obj_ads, name='url_user_ads'),
]
