from django.shortcuts import render

# Create your views here.
def signup(request):
	return render(request, 'signup.html', {})

def signup_confirm(request):
	return render(request, 'signup_confirm.html', {})

def login(request):
	return render(request, 'login.html', {})

def logout(request):
	pass

def profile(request):
	return render(request, 'profile.html', {})
