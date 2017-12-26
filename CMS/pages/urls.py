from django.conf.urls import url
from .views import custom_page, main_page


urlpatterns = [
    url(r'^$', main_page, name='url_main_page'),
    url(r'^page_(?P<pk>\d+)/$', custom_page, name='custom_page'),
]
