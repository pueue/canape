from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^create/$', views.postageCreate, name='postageCreate'),
	url(r'^detail/(?P<postage_id>\d+)/$', views.postageDetail, name='postageDetail'),
]
