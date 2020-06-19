from django import forms
from jobApp.models import Hyderabad_jobs,Mumbai_jobs,Pune_jobs,Bangalore_jobs

class hydjobsForm(forms.ModelForm):
    class Meta:
        model=Hyderabad_jobs
        fields='__all__'
class punejobsForm(forms.ModelForm):
    class Meta:
        model=Pune_jobs
        fields='__all__'
class mumbaijobsForm(forms.ModelForm):
    class Meta:
        model=Mumbai_jobs
        fields='__all__'
class bangalorejobsForm(forms.ModelForm):
    class Meta:
        model=Bangalore_jobs
        fields='__all__'
