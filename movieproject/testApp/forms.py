from django import forms
from testApp.models import MovieInfo

class MovieForm(forms.ModelForm):
    class Meta:
        model=MovieInfo
        fields='__all__'