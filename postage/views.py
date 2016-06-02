from django.shortcuts import render
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

# def postageDetail(request):
# 	return render(request, 'postageDetail.html', {})
