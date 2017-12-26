from django.conf.urls import url
from .views import (
    view_list,
    view_obj,
    view_obj_add,
    view_obj_edit,
    view_draft_list,
    view_draft_add,
    view_draft_edit,
)


urlpatterns = [
    url(r'^(?:page_(?P<page_number>\d+)/)?$', view_list, name='entry_list'),
    url(r'^(?P<pk>\d+)/$', view_obj, name='url_entry_obj'),
    url(r'^add/$', view_obj_add, name='url_entry_add'),
    url(r'^(?P<pk>\d+)/edit/$', view_obj_edit, name='url_entry_edit'),
    url(r'^drafts/(?:page_(?P<page_number>\d+)/)?$', view_draft_list, name='url_entry_draft_list'),
    url(r'^drafts/add/$', view_draft_add, name='url_entry_draft_add'),
    url(r'^drafts/(?P<pk>\d+)/$', view_draft_edit, name='url_entry_draft_edit'),
]
