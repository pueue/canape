from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/$', views.canape_create, name='canape_create'),
    url(r'^detail/(?P<canape_id>\d+)/$', views.canape_detail, name='canape_detail'),
    url(r'^edit/(?P<canape_id>\d+)/$', views.canape_edit, name='canape_edit'),
    url(r'^delete/(?P<canape_id>\d+)/$', views.canape_delete, name='canape_delete'),

    url(r'^code/(?P<code_id>\d+)/$', views.code_detail, name='code_detail')
]
