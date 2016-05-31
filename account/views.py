from django.shortcuts import render, redirect
from .forms import SignupForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import User

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

def profile(request, username):
	try:
		user = User.objects.get(username=username)
	except User.DoesNotExist:
		return redirect('home')
	return render(request, 'profile.html', {'user': user})
