from django import forms
class StudentRegister(forms.Form):
    name=forms.CharField()
    marks=forms.IntegerField()
