from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^create/$', views.postageCreate, name='postageCreate'),
	url(r'^detail/(?P<postage_id>\d+)/$', views.postageDetail, name='postageDetail'),
	url(r'^edit/(?P<postage_id>\d+)/$', views.postageEdit, name='postageEdit'),
	url(r'^delete/(?P<postage_id>\d+)/$', views.postageDelete, name='postageDelete'),

	url(r'^code/(?P<code_id>\d+)/$', views.codeDetail, name='codeDetail')
]
