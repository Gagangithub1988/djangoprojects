from django.shortcuts import render
from . import forms
# Create your views here.
def studentview(request):
    form=forms.StudentForm()
    if request.method=='POST':
        form=forms.StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print('Form data insterted into database successfully')

    return render(request,"testApp/register.html",{'form':form})
