from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^signup_confirm/$', TemplateView.as_view(
			template_name="signup_confirm.html"
		), name='signup_confirm'),
	url(r'^login/$', auth_views.login, {
			# 'template_name': 'login.html',
		}, name='login'),
	url(r'^logout/$', auth_views.logout, {
			'next_page': 'login',
		}, name='logout'),
	url(r'^profile/(?P<username>\w+)/$', views.profile, name='profile'),
]
