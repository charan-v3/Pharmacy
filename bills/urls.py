from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path("", views.bill_summary, name="bill_summary"),
    path("add/", views.bill_add, name="bill_add"),
    path("delete/", views.bill_delete, name="bill_delete"),
    path("update/", views.bill_update, name="bill_update"),
]
