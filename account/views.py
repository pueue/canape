from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, LoginForm, SettingsForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import User
from canape.models import Canape, Code
from django.contrib.auth.views import login as auth_login
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                email=form.cleaned_data['email'],
                username=form.cleaned_data['username'],
                name=form.cleaned_data['name'],
                password=form.cleaned_data['password1'],
            )
            return HttpResponseRedirect(reverse("register_confirm"))
    else:
        form = RegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


def register_confirm(request):
    context = {}
    return render(request, 'register_confirm.html', context)


def login(request):
    form = LoginForm(data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            auth_login(request, form.user)
            return HttpResponseRedirect(reverse("home"))
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)


def profile(request, username):
    user = get_object_or_404(User, username=username)
    works = Canape.objects.filter(maker=user)
    achievements = Code.objects.filter(gainer=user)

    context = {
        'user': user,
        'works': works,
        'achievements': achievements,
    }
    return render(request, 'profile.html', context)


@login_required
def settings(request):
    if request.method == "POST":
        form = SettingsForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("profile", kwargs={
                'username': request.user.username,
            }))
    else:
        form = SettingsForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'settings.html', context)
