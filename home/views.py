from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import medicine
from .forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm

data = {"medicines": medicine.objects.all(), "title": "Home"}

def home(request):
    return render(request, "home/customerHome.html", data)


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request,
                f"You are ready to user Your Account ! You can login here {username}!",
            )
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "home/register.html", {"form": form})
