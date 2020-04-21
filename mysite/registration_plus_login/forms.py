from django import forms
from django.forms import ModelForm
from django.contrib.auth.admin import User
from .models import UserInfo 
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = User
        fields = ('first_name','last_name','username','password')

class UserInfoForm(forms.ModelForm):
    class Meta():
        model = UserInfo
        fields = ('bio','email')
