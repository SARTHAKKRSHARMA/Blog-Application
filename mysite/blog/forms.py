from django import forms
from .models import *
from django.forms import ModelForm


class New_Blog(forms.ModelForm):
    class Meta():
        model = Blog_Detail
        fields = ('title','body')

class Update_Blog(forms.ModelForm):
    class Meta():
        model = Blog_Detail
        fields = ('body',)