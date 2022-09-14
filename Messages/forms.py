from django import forms


class SendMessageForm(forms.Form):

    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))


class SearchUserForm(forms.Form):

    user_name = forms.CharField()
    #user_name = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
