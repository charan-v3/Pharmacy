from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path("", views.bill_summary, name="bill_summary"),
    path("create_bill/", views.create_bill, name="create_bill"),
    path("add_item_to_bill/", views.add_item_to_bill, name="add_item_to_bill"),
]
