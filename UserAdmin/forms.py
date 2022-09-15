from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.PasswordInput(attrs={'class': 'form-control'})

    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegisterForm(UserCreationForm):

    username = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UserEditForm(forms.Form):

    first_name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))


class ProfileEditForm(forms.Form):

    webpage = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))


class ImageEditForm(forms.Form):

    imagen = forms.ImageField()

