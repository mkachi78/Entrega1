from django import forms

class UserForm(forms.Form):
    name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

class PublicationForm(forms.Form):
    author = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

class SearchForm(forms.Form):
    search_values = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))