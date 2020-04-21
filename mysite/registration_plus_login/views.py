from django import forms
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.admin import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import UserForm,UserInfoForm

# Create your views here.
def registration(request):
    user_form = UserForm()
    user_info_form = UserInfoForm()
    return render(request,'registration_plus_login/register.html',
                    {'user_form':user_form,'user_info_form':user_info_form})

def c_registration(request):
    if request.POST:
        user_form = UserForm(request.POST)
        user_info_form = UserInfoForm(request.POST)

        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = user_info_form.save(commit=False)
            profile.user = user
            profile.save()
            return HttpResponseRedirect(reverse('homepage'))
        
        else:
            raise forms.ValidationError('Invalid detail')
    else:
        return HttpResponseRedirect(reverse('registration'))

def request_login(request):
    return render(request,'registration_plus_login/login.html')


def user_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)

        if user:
            login(request,user)
            return HttpResponseRedirect(reverse('homepage'))
        else:
            raise forms.ValidationError('Invalid Credintial')
    else:
        return HttpResponseRedirect(reverse('request_login'))

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))