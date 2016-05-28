from django.shortcuts import render

# Create your views here.
def signup(request):
	return render(request, 'signup.html', {})

def signup_confirm(request):
	return render(request, 'signup_confirm.html', {})

def profile(request):
	return render(request, 'profile.html', {})
