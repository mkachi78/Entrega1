from django import forms

class PagesForm(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    imagen = forms.ImageField()
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))