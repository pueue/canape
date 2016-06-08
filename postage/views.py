from django.shortcuts import render, redirect
from .forms import CreateForm, EditForm
from .models import Postage
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
	try:
		postage = Postage.objects.get(id=postage_id);
	except Postage.DoesNotExist:
		return redirect('home')

	context = {
		'postage': postage,
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

def postageDelete(request, postage_id):
	postage = Postage.objects.get(pk=postage_id)
	if postage.maker != request.user:
		return redirect('home')

	postage.delete()
	return HttpResponseRedirect(reverse("profile", kwargs={
		'username': request.user.username,
	}))
