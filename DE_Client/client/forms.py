from django import forms
from django.forms import ModelForm
from client.formModels import *


class userLoginForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'PASSWORD'}), label='', required=True)
    userID_email = forms.CharField(required=True, label='',
                                   widget=forms.TextInput(attrs={'placeholder': 'USER ID / EMAIL'}))
    class Meta:
        model = userLogin
        fields = '__all__'

