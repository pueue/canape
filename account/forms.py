from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
from .models import User
from django.contrib.auth import authenticate


class RegisterForm(UserCreationForm):
    username = forms.RegexField(
        label="Username",
        max_length=20,
        regex=r'^[\w.-]+$',
        help_text = "20 characters or fewer. Letters, digits and ./-/_ only.",
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'required': 'true',
            'class': 'form-control',
        }))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email',
            'required': 'true',
            'class': 'form-control',
        }))
    name = forms.CharField(
        label="Name",
        widget=forms.TextInput(attrs={
            'placeholder': 'Name',
            'required': 'true',
            'class': 'form-control',
        }))
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'required': 'true',
            'class': 'form-control',
        }),)
    password2 = forms.CharField(
        label="Password (again)",
        strip=False,
        widget=forms.PasswordInput(attrs={
                'placeholder': 'Password (again)',
                'required': 'true',
                'class': 'form-control',
        }),)

    class Meta:    # ModelForm은 class Meta를 반드시 정의해줘야 한다.
        model = User
        fields = ("username", "email", "name", "password1", "password2",)


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        max_length=20,
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'required': 'true',
            'class': 'form-control',
            'autofocus': 'true'
        }))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'required': 'true',
            'class': 'form-control',
        }))

    def clean(self):
        username = self.cleaned_data.get('username')
        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            self.add_error('username', 'No such username')
            raise forms.ValidationError("No Such User Error")
        password = self.cleaned_data.get('password')
        self.user = authenticate(username=username, password=password)
        if self.user is None or not self.user.is_active:
            self.add_error('password', 'Password is incorrect')
            raise forms.ValidationError('Incorrect Password Error')
        return self.cleaned_data


class SettingsForm(forms.ModelForm):
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email',
            'class': 'form-control',
        }))
    name = forms.CharField(
        label="Name",
        widget=forms.TextInput(attrs={
            'placeholder': 'Name',
            'required': 'true',
            'class': 'form-control',
        }))
    image = forms.ImageField(
        label="Image",
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'form-control',
        }))
    description = forms.CharField(
        label="Description",
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Description',
            'class': 'form-control',
        }))

    class Meta:
        model = User
        fields = ('email', 'name', 'image', 'description', )
