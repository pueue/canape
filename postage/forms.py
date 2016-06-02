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
	image = forms.ImageField(label="Image",
		widget=forms.FileInput(attrs={
			'required': 'true',
			'class': 'form-control',
		}))
	description = forms.CharField(label="Description",
		widget=forms.TextInput(attrs={
			'placeholder': 'description',
			'required': 'true',
			'class': 'form-control',
		}))
	is_transferable = forms.BooleanField(label="is_transferable",
		widget=forms.CheckboxInput(attrs={
			'class': 'form-control',
		}))
	is_limit = forms.BooleanField(label="is_limit",
		widget=forms.CheckboxInput(attrs={
			'class': 'form-control',
		}))
	quantity = forms.IntegerField(label="quantity",
		widget=forms.NumberInput(attrs={
			'class': 'form-control',
		}))

	class Meta:
		model = Postage
		fields = ("title", "image", "description", "is_transferable", "is_limit", "quantity")
