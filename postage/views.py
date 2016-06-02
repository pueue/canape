from django.shortcuts import render
from .forms import PostageForm
from django.http import HttpResponseRedirect

# Create your views here.
def postageCreate(request):
	form = PostageForm()
	if request.method == "POST":
		form = PostageForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('postageDetail')
	context = {
		'form': form,
	}
	return render(request, 'postageCreate.html', context)

# def postageDetail(request):
# 	return render(request, 'postageDetail.html', {})
