from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^new/$', views.canape_new, name='canape_new'),
    url(r'^(?P<canape_id>\d+)/$', views.canape_detail, name='canape_detail'),
    url(r'^(?P<canape_id>\d+)/edit/$', views.canape_edit, name='canape_edit'),
    url(r'^(?P<canape_id>\d+)/delete/$', views.canape_delete, name='canape_delete'),
    url(r'^(?P<canape_id>\d+)/(?P<code_serial>\d+)/$', views.code_detail, name='code_detail'),

    url(r'^get/$', views.code_verify, name='code_verify')
]
