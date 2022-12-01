from django import forms

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    username = forms.CharField(max_length=150)
    email = forms.CharField(max_length=254)
    password1 = forms.CharField(max_length=128)
    password2 = forms.CharField(max_length=128)