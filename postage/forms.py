from django import forms
from .models import Postage

class PostageForm(forms.ModelForm):
	title = forms.CharField(label="Title",
		max_length=200,
		widget=forms.TextInput(attrs={
		    'placeholder': 'title',
		    'required': 'true',
			'class': 'form-control',
        }))
	image = forms.ImageField(label="Image",)
	description = forms.CharField(label="Description")
	is_transferable = forms.BooleanField(label="is_transferable")
	is_limit = forms.BooleanField(label="is_limit")
	quantity = forms.IntegerField(label="quantity")

	class Meta:
		model = Postage
		fields = ("title", "image", "description", "is_transferable", "is_limit", "quantity")
