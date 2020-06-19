from django import forms
from django.core import validators

"""def start_with(value):
    if value[0].lower() != 'd':
        raise forms.ValidationError('Name should be start with d')
"""
class feedback(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(label='Password(Again)',widget=forms.PasswordInput)
    bot_handler=forms.CharField(required=False,widget=forms.HiddenInput)
    feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])

    def clean(self):
        print('Total form validation')
        cleaned_data=super().clean()
        inputname=cleaned_data['name']

        if len(inputname) <10:
            raise forms.ValidationError('Name should be morethan 10 char')
        inputrollno=cleaned_data['rollno']
        if len(str(inputrollno)) != 3:
            raise forms.ValidationError('Rollno should contain exactly three digit')
        inputpasswrd=cleaned_data['password']
        inputrpasswrd=cleaned_data['rpassword']
        if inputpasswrd != inputrpasswrd:
            raise forms.ValidationError('Password is not matching')
        bot_handler_value=cleaned_data['bot_handler']
        if len(bot_handler_value)>0:
            raise forms.ValidationError('Thanks Bot...')
