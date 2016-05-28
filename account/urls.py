from django.conf.urls import url
from . import views, forms
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^signup_confirm/$', views.signup_confirm, name='signup_confirm'),
	url(r'^login/$', auth_views.login, {
			'template_name': 'login.html',
		}, name='login'),
	url(r'^logout/$', auth_views.logout, {
			'next_page': 'login',
		}, name='logout'),
	url(r'^profile/(?P<username>\w+)/$', views.profile, name='profile'),
]
