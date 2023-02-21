from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("adminDashboard/", views.adminDashboardIndex, name="adminDashboardIndex"),
    path("button/", views.button, name="button"),
    path("blank/", views.blank, name="blank"),
    path("chart/", views.chart, name="chart"),
    path("element/", views.element, name="element"),
    path("form/", views.form, name="form"),
    path("table/", views.table, name="table"),
    path("typography/", views.typography, name="typography"),
    path("widget/", views.widget, name="widget"),
]
