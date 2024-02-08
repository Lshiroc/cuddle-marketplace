from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full p-2 mb-4 outline-purple-300',
        'placeholder': 'Your username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full p-2 mb-4 outline-purple-300',
        'placeholder': 'Your password'
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full p-2 mb-4 outline-purple-300',
        'placeholder': 'Your username'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'w-full p-2 mb-4 outline-purple-300',
        'placeholder': 'Your email'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full p-2 mb-4 outline-purple-300',
        'placeholder': 'Your password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full p-2 mb-4 outline-purple-300',
        'placeholder': 'Password again'
    }))
