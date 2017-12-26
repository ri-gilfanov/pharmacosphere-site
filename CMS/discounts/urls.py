from django.conf.urls import url
from .views import (
    view_list,
)


urlpatterns = [
    url(r'^$', view_list, name='discount_list'),
]
