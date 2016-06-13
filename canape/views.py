from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .forms import CanapeNewForm, CanapeEditForm
from .models import Canape, Code

@login_required
def canape_new(request):
    form = CanapeNewForm()
    if request.method == "POST":
        form = CanapeNewForm(request.POST, request.FILES)
        if form.is_valid():
            canape = form.save(commit=False)
            canape.maker = request.user
            canape.save()
            return HttpResponseRedirect(reverse("canape_detail", kwargs={
                'canape_id': canape.id,
            }))
    context = {
        'form': form,
    }
    return render(request, 'canape_new.html', context)


def canape_detail(request, canape_id):
    canape = get_object_or_404(Canape, id=canape_id)
    used_quantity = Code.objects.filter(canape=canape).count()
    residual_quantity = canape.quantity - used_quantity

    context = {
        'canape': canape,
        'residual_quantity': residual_quantity,
    }
    return render(request, 'canape_detail.html', context)


@login_required
def canape_edit(request, canape_id):
    canape = get_object_or_404(Canape, id=canape_id)
    if canape.maker != request.user:
        return redirect('home')

    if request.method == "POST":
        form = CanapeEditForm(request.POST, request.FILES, instance=canape)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("canape_detail", kwargs={
                'canape_id': canape.id,
            }))
    else:
        form = CanapeEditForm(instance=canape)
    context = {
        'canape': canape,
        'form': form,
    }
    return render(request, 'canape_edit.html', context)


def canape_delete(request, canape_id):
    canape = get_object_or_404(Canape, id=canape_id)
    if canape.maker != request.user:
        return redirect('home')

    canape.delete()
    return HttpResponseRedirect(reverse("profile", kwargs={
        'username': request.user.username,
    }))


def code_detail(request, canape_id, code_serial):
    canape = get_object_or_404(Canape, id=canape_id)
    code = get_object_or_404(Code, canape=canape, serial=code_serial)
    context = {
        'code': code,
    }
    return render(request, 'code_detail.html', context)
