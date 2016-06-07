from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class SignupForm(UserCreationForm):
	username = forms.RegexField(label="Username",
		max_length=20,
		regex=r'^[\w.@+-]+$',
		help_text = "Required. 30 characters or fewer. Letters, digits and "
        "@/./+/-/_ only.",
		widget=forms.TextInput(attrs={
		    'placeholder': 'Username',
		    'required': 'true',
			'class': 'form-control',
        }))
	email = forms.EmailField(widget=forms.EmailInput(attrs={
			'placeholder': 'Email',
			'required': 'true',
			'class': 'form-control',
		}))
	name = forms.CharField(label="Name",
		widget=forms.TextInput(attrs={
			'placeholder': 'Name',
			'required': 'true',
			'class': 'form-control',
		}))
	password1 = forms.CharField(label="Password",
		strip=False,
		widget=forms.PasswordInput(attrs={
		    'placeholder': 'Password',
		    'required': 'true',
			'class': 'form-control',
	    }),)
	password2 = forms.CharField(label="Password confirmation",
		strip=False,
		widget=forms.PasswordInput(attrs={
		        'placeholder': 'Password confirmation',
		        'required': 'true',
				'class': 'form-control',
	    }),
		help_text = "Enter the same password as above, for verification.")

	class Meta:	# ModelForm은 class Meta를 반드시 정의해줘야 한다.
		model = User
		fields = ("username", "email", "name", "password1", "password2",)

class LoginForm(AuthenticationForm):
	username = forms.CharField(label="Username",
		max_length=20,
		widget=forms.TextInput(attrs={
			'placeholder': 'Username',
			'required': 'true',
			'class': 'form-control',
			'autofocus': 'true'
		}))
	password = forms.CharField(label="Password",
		strip=False,
		widget=forms.PasswordInput(attrs={
			'placeholder': 'Password',
			'required': 'true',
			'class': 'form-control',
		}))

class settingsForm(forms.ModelForm):
	email = forms.EmailField(label="Email",
		required=True,
		widget=forms.EmailInput(attrs={
			'placeholder': 'Email',
			'class': 'form-control',
		}))
	name = forms.CharField(label="Name",
		widget=forms.TextInput(attrs={
			'placeholder': 'Name',
			'required': 'true',
			'class': 'form-control',
		}))
	image = forms.ImageField(label="Image",
		required=False,
		widget=forms.FileInput(attrs={
			'class': 'form-control',
		}))
	description = forms.CharField(label="Description",
		required=False,
		widget=forms.TextInput(attrs={
			'placeholder': 'Description',
			'class': 'form-control',
		}))
	class Meta:
		model = User
		fields = ('email', 'name', 'image', 'description', )
