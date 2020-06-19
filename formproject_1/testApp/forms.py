from django import forms

class RegisterForm(forms.Form):
    first_name=forms.CharField(max_length=20)
    last_name=forms.CharField(max_length=20)
