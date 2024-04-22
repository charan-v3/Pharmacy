from django.shortcuts import render
from django.http import HttpResponse
from .models import medicine

data = {"medicines": medicine.objects.all(), "title": "Home"}

def home(request):
    return render(request, "home/home.html", data)
