from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer
from django import forms


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields  = '__all__'
        # exclude = ['user']
        # exclude = ['user', 'email','name', 'otp_code']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields  = ['username', 'password1', 'password2']