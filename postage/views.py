from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateForm, EditForm
from .models import Postage, Code
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required
def postage_create(request):
    form = CreateForm()
    if request.method == "POST":
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            postage = form.save(commit=False)
            postage.maker = request.user
            postage.save()
            return HttpResponseRedirect(reverse("postage_detail", kwargs={
                'postage_id': postage.id,
            }))
    context = {
        'form': form,
    }
    return render(request, 'postage_create.html', context)


def postage_detail(request, postage_id):
    postage = get_object_or_404(Postage, id=postage_id)
    used_quantity = Code.objects.filter(postage=postage).count()
    residual_quantity = postage.quantity - used_quantity

    context = {
        'postage': postage,
        'residual_quantity': residual_quantity,
    }
    return render(request, 'postage_detail.html', context)


@login_required
def postage_edit(request, postage_id):
    postage = Postage.objects.get(pk=postage_id)
    if postage.maker != request.user:
        return redirect('home')

    if request.method == "POST":
        form = EditForm(request.POST, request.FILES, instance=postage)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("postage_detail", kwargs={
                'postage_id': postage.id,
            }))
    else:
        form = EditForm(instance=postage)
    context = {
        'postage': postage,
        'form': form,
    }
    return render(request, 'postage_edit.html', context)


def postage_delete(request, postage_id):
    postage = Postage.objects.get(pk=postage_id)
    if postage.maker != request.user:
        return redirect('home')

    postage.delete()
    return HttpResponseRedirect(reverse("profile", kwargs={
        'username': request.user.username,
    }))


def code_detail(request, code_id):
    code = get_object_or_404(Code, id=code_id)
    context = {
        'code': code,
    }
    return render(request, 'code_detail.html', context)
