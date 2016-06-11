from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm, LoginForm, SettingsForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import User
from canape.models import Canape, Code
from django.contrib.auth.views import login as auth_login
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("signup_confirm"))
    else:
        form = SignupForm()
    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)


def signup_confirm(request):
    context = {}
    return render(request, 'signup_confirm.html', context)


def login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect(reverse("home"))
            else:
                print("Wrong username or password")
                return HttpResponseRedirect(reverse("login"))
    else:
        form = LoginForm()
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
