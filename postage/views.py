from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateForm, EditForm
from .models import Postage, Code
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def postageCreate(request):
	form = CreateForm()
	if request.method == "POST":
		form = CreateForm(request.POST, request.FILES)
		if form.is_valid():
			postage = form.save(commit=False)
			postage.maker = request.user
			postage.save()
			return HttpResponseRedirect(reverse("postageDetail", kwargs={
				'postage_id': postage.id,
			}))
	context = {
		'form': form,
	}
	return render(request, 'postageCreate.html', context)

def postageDetail(request, postage_id):
	postage = get_object_or_404(Postage, id=postage_id);
	used_quantity = Code.objects.filter(postage=postage).count();
	residual_quantity = postage.quantity - used_quantity;

	context = {
		'postage': postage,
		'residual_quantity': residual_quantity,
	}
	return render(request, 'postageDetail.html', context)

@login_required
def postageEdit(request, postage_id):
	postage = Postage.objects.get(pk=postage_id)
	if postage.maker != request.user:
		return redirect('home')

	if request.method == "POST":
		form = EditForm(request.POST, request.FILES, instance=postage)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("postageDetail", kwargs={
				'postage_id': postage.id,
			}))
	else:
		form = EditForm(instance=postage)
	context = {
		'postage': postage,
		'form': form,
	}
	return render(request, 'postageEdit.html', context)

	postage = Postage.objects.get(pk=postage_id)
def postageDelete(request, postage_id):
	if postage.maker != request.user:
		return redirect('home')

	postage.delete()
	return HttpResponseRedirect(reverse("profile", kwargs={
		'username': request.user.username,
	}))

def codeDetail(request, code_id):
	code = get_object_or_404(Code, id=code_id)
	context = {
		'code': code,
	}
	return render(request, 'codeDetail.html', context);
