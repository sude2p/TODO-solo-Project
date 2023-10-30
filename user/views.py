from django.shortcuts import render, redirect
from base.models import Task
from base.modelform import TaskForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.contrib import messages
from .user_form import UserLogin,CustomUserCreationForm
from base.urls import *





# Create your views here.

def userLogin(request):
    userform = UserLogin
    context = {'form': userform}
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'username doesnot exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'username or password is incorrect' )
    
    return render(request,'user/user_login.html', context)

def userLogout(request):
    logout(request)
    messages.error(request, 'user successfully logged out')
    return redirect('login')

def userRegister(request):
    if request.method == 'POST':
        registration_form = CustomUserCreationForm(request.POST)
        if registration_form.is_valid():
            user = registration_form.save()
            user.username = user.username.lower()
            user.save()
            return redirect('login')
        else:
            messages.error(request, 'Invalid input')    
    else:
        registration_form = CustomUserCreationForm()
    context = {'form': registration_form}
    return render(request, 'user/user_register.html', context)
