from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home/home.html')


def signup(request):
    return render(request, "home/signup.html")
