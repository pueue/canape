from django.shortcuts import render
from .forms import SignupForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
def signup(request):
	form = SignupForm()
	if request.method == "POST":
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("signup_confirm"))
	return render(request, 'signup.html', {"form": form,})

def signup_confirm(request):
	return render(request, 'signup_confirm.html', {})

def profile(request):
	return render(request, 'profile.html', {})
