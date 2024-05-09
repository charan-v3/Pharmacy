from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import medicine, Profile
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

data = {"medicines": medicine.objects.all(), "title": "Home"}
profiles = {"profile": Profile.objects.first(), "title": "Profile Page"}

def home(request):
    return render(request, "home/customerHome.html", data)


@login_required
def profileview(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account has been Updated !")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {"u_form": u_form, "p_form": p_form}
    return render(request, "home/profile.html", context)


def about(request):
    return render(request, "home/about.html")


def contact(request):
    return render(request, "home/contact.html")

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = user.username
            messages.success(
                request,
                f"You are ready to use Your Account! You can log in here {username}!",
            )
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "home/register.html", {"form": form})
