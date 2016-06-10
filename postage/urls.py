from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/$', views.postage_create, name='postage_create'),
    url(r'^detail/(?P<postage_id>\d+)/$', views.postage_detail, name='postage_detail'),
    url(r'^edit/(?P<postage_id>\d+)/$', views.postage_edit, name='postage_edit'),
    url(r'^delete/(?P<postage_id>\d+)/$', views.postage_delete, name='postage_delete'),

    url(r'^code/(?P<code_id>\d+)/$', views.code_detail, name='code_detail')
]
