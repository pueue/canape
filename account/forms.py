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
        }))
	email = forms.EmailField(widget=forms.EmailInput(attrs={
			'placeholder': 'Email',
			'required': 'True',
		}))
	password1 = forms.CharField(label="Password",
		strip=False,
		widget=forms.PasswordInput(attrs={
		    'placeholder': 'Password',
		    'required': 'true',
	    }),)
	password2 = forms.CharField(label="Password confirmation",
		strip=False,
		widget=forms.PasswordInput(attrs={
		        'placeholder': 'Password confirmation',
		        'required': 'true',
	    }),
		help_text = "Enter the same password as above, for verification.")

	class Meta:	# ModelForm은 class Meta를 반드시 정의해줘야 한다.
		model = User
		fields = ("username", "email", "password1", "password2",)

# class LoginForm(AuthenticationForm):
# 	username = forms.CharField(label="Username",
# 		max_length=30,
# 		width=forms.TextInput(attrs={
# 			'placeholder': 'Username',
# 			'required': 'True',
# 		}))
# 	password = forms.CharField(label="Password",
# 		strip=False,
# 		widget=forms.PasswordInput(attrs={
# 			'placeholder': 'Password',
# 			'required': 'True',
# 		}))
