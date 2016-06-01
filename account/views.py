from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import User
from postage.models import Postage, Code;
from django.contrib import auth

# Create your views here.
def signup(request):
	form = SignupForm()
	if request.method == "POST":
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("signup_confirm"))
	context = {
		'form': form,
	}
	return render(request, 'signup.html', context)

def signup_confirm(request):
	context = {}
	return render(request, 'signup_confirm.html', context)

def login(request):
	form = LoginForm()
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			user = form.get_user()
			if user is not None:
				auth.login(request, user)
				return HttpResponseRedirect(reverse("home"))
			else:
				return HttpResponseRedirect(reverse("login"))
	context = {
		'form': form,
	}
	return render(request, 'login.html', context)

def profile(request, username):
	try:
		user = User.objects.get(username=username)
		works = Postage.objects.filter(maker=user)
		achievements = Code.objects.filter(gainer=user)
	except User.DoesNotExist:
		return redirect('home')
	context = {
		'user': user,
		'works': works,
		'achievements': achievements,
	}
	return render(request, 'profile.html', context)
