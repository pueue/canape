from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
# from .forms import LoginForm

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^register_confirm/$', TemplateView.as_view(
            template_name="register_confirm.html"
        ), name='register_confirm'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {
            'next_page': 'login',
        }, name='logout'),
    url(r'^settings/$', views.settings, name='settings'),

    url(r'^(?P<username>\w+)/$', views.profile, name='profile'),
]
