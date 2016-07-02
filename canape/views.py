from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db import transaction

from .forms import NewCanapeForm, EditCanapeForm, VerifyCodeForm, DistributeCodeForm
from .models import Canape, Code
from .function import generate_code, distribute_code


@transaction.atomic
@login_required
def canape_new(request):
    form = NewCanapeForm()
    if request.method == "POST":
        form = NewCanapeForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                with transaction.atomic():
                    canape = form.save(commit=False)
                    canape.maker = request.user
                    canape.save()
                    if canape.is_limit:
                        generate_code(canape, canape.quantity)
            except:
                return redirect('home')
            return HttpResponseRedirect(reverse("canape_detail", kwargs={
                'canape_id': canape.id,
            }))
    context = {
        'form': form,
    }
    return render(request, 'canape_new.html', context)


def canape_detail(request, canape_id):
    canape = get_object_or_404(Canape, id=canape_id)
    used_quantity = Code.objects.filter(
        canape=canape, gainer__isnull=False).count()
    residual_quantity = canape.quantity - used_quantity

    if request.method == "POST":
        form = DistributeCodeForm(request.POST)
        if form.is_valid():
            emails = form.cleaned_data['emails']
            distribute_code(canape, emails)
            return redirect('home')
    else:
        form = DistributeCodeForm()
    context = {
        'canape': canape,
        'residual_quantity': residual_quantity,
        'form': form,
    }
    return render(request, 'canape_detail.html', context)


@login_required
def canape_edit(request, canape_id):
    canape = get_object_or_404(Canape, id=canape_id)
    if canape.maker != request.user:
        return redirect('home')

    if request.method == "POST":
        form = EditCanapeForm(request.POST, request.FILES, instance=canape)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("canape_detail", kwargs={
                'canape_id': canape.id,
            }))
    else:
        form = EditCanapeForm(instance=canape)
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


@login_required
def code_verify(request):
    if request.method == "POST":
        form = VerifyCodeForm(request.POST)
        if form.is_valid():
            try:
                code = Code.objects.get(code=form.cleaned_data['code'])
                code.gainer = request.user
                code.save()
            except:
                return HttpResponseRedirect(reverse('profile', kwargs={
                    'username': request.user.username,
                }))
    else:
        form = VerifyCodeForm()
    context = {
        'form': form,
    }
    return render(request, 'code_verify.html', context)


def code_detail(request, canape_id, code_serial):
    canape = get_object_or_404(Canape, id=canape_id)
    code = get_object_or_404(Code, canape=canape, serial=code_serial)
    context = {
        'code': code,
    }
    return render(request, 'code_detail.html', context)
