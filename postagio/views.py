from django.shortcuts import render
from postage.models import Postage
from account.models import User


def home(request):
    context = {}
    return render(request, 'home.html', context)
