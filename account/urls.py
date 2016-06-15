from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
# from .forms import LoginForm

urlpatterns = [
    # REST url
    # url(r'^users/new/$', views.register, name='users_new'),
    # url(r'^users/new/confirm/$', TemplateView.as_view(
    #         template_name="register_confirm.html"
    #     ), name='user_new_confirm'),
    # url(r'^(?P<username>\w+)/edit/$', view.settings, name='user_edit'),
    # url(r'^session/new/$', views.login, name='session_new'),
    # url(r'^session/delete/$', auth_views.logout, {
    #         'next_page': 'session_new',
    #     }, name='session_delete'),

    url(r'^register/$', views.register, name='register'),
    url(r'^register_confirm/$', TemplateView.as_view(
            template_name="register_confirm.html"
        ), name='register_confirm'),
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {
            'next_page': 'login',
        }, name='logout'),

    url(r'^(?P<username>\w+)/$', views.profile, name='profile'),
]
