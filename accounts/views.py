from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from .forms import CreateUserForm, CustomerForm
from django.contrib.auth.decorators import login_required
import os
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def registerPage(request):
    form = CreateUserForm()
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+user)
            return redirect('login')
        else:
            messages.error(request, "Password do not match!")
        context = {'form':form}
        
    return render(request, 'signup.html', context)




def loginUser(request):
    context = {}   
    return render(request, 'login.html', context)

def howItWork(request):
    context = {}   
    return render(request, 'accounts/howItWork.html', context)

def service(request):
    context = {}   
    return render(request, 'accounts/service.html', context)

def booking(request):
    context = {}   
    return render(request, 'accounts/booking.html', context)


def home(request):
    return render(request, 'accounts/index.html')

def findDoctors(request):
    return render(request, 'accounts/doctors.html')

def videoConsult(request):
    return render(request, 'accounts/videoConsult.html')


def loginUser_V1(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        try:
            if user is not None:
                login(request, user)
                messages.success(request, f' Wecome {username}')
                return redirect("/")
            else:
                messages.error(request, "Wrong Credentials!!")
                return render(request,'login_V1.html')
        except:
            messages.error(request, "Please enter email and password for login!")
            return render(request,'login_V1.html')
    context={}
    return render(request, 'accounts/login_V1.html')




