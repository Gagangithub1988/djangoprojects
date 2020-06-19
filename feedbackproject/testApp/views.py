from django.shortcuts import render
from . import forms
# Create your views here.
def feedbackview(request):
    form=forms.feedback()
    if request.method=='POST':
        form=forms.feedback(request.POST)
        if form.is_valid():
            print('Validation completed...printing feedback info')
            print('Student name:',form.cleaned_data['name'])
            print('Student Roll No:',form.cleaned_data['rollno'])
            print('Student Email:',form.cleaned_data['email'])
            print('Student Feedback:',form.cleaned_data['feedback'])
    return render(request,'testApp/feedback.html',{'form':form})
