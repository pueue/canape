from django.shortcuts import render
from canape.models import Canape
from account.models import User


def home(request):
    context = {}
    return render(request, 'home.html', context)
