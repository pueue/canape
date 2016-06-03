from django.shortcuts import render, redirect
from .forms import PostageForm
from .models import Postage
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def postageCreate(request):
	form = PostageForm()
	if request.method == "POST":
		form = PostageForm(request.POST, request.FILES)
		if form.is_valid():
			postage = form.save(commit=False)
			postage.maker = request.user
			postage.save()
			return HttpResponseRedirect('postageDetail')
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
