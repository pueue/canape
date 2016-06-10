from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
# from .forms import LoginForm

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signup_confirm/$', TemplateView.as_view(
            template_name="signup_confirm.html"
        ), name='signup_confirm'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {
            'next_page': 'login',
        }, name='logout'),
    url(r'^settings/$', views.settings, name='settings'),

    url(r'^(?P<username>\w+)/$', views.profile, name='profile'),
]
