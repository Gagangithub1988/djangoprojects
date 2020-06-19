from django import forms
from formApp.models import Volunteer

class VolunteerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=Volunteer
        fields='__all__'
