
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User


def adminDashboardIndex(request):
    return render(request,"adminDashboard/index.html")


def button(request):
    return render(request,"adminDashboard/button.html")


def blank(request):
    return render(request,"adminDashboard/blank.html")

def chart(request):
    return render(request,"adminDashboard/chart.html")


def element(request):
    return render(request,"adminDashboard/element.html")

def form(request):
    return render(request,"adminDashboard/form.html")

def table(request):
    return render(request,"adminDashboard/table.html")

def typography(request):
    return render(request,"adminDashboard/typography.html")

def widget(request):
    return render(request,"adminDashboard/widget.html")

