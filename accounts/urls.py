from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('findDoctors/', views.findDoctors, name="findDoctors"),
    path('videoConsult/', views.videoConsult, name="videoConsult"),
    path('howItWork/', views.howItWork, name="howItWork"),
    path('service/', views.service, name="service"),
    path('booking/', views.booking, name="booking"),
    path('login_V1/',views.loginUser_V1, name="login_V1"),
    path('login/',views.loginUser, name="login"),
    path('signup/',views.registerPage, name="signup"),
]
