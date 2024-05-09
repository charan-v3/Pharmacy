from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import medicine, Profile
from django.views.generic import ListView
from .forms import (
    UserRegisterForm,
    ProfileUpdateForm,
    UserUpdateForm,
    InsuranceUpdateForm,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

data = {
    "medicines": medicine.objects.all(),
    "title": "Home",
    "profiles": Profile.objects.filter(user_type="Customer"),
}
profiles = {"profile": Profile.objects.first(), "title": "Profile Page"}

def home(request):
    if not request.user.is_authenticated:
        return render(request, "home/customerHome.html", data)

    if request.user.profile.user_type == "Customer":
        return render(request, "home/customerHome.html", data)
    else:
        return render(request, "home/workerHome.html", data)


class PostListView(ListView):
    model = medicine
    context_object_name = "medicines"
    ordering = ["drugname"]

    def get_template_names(self):
        if (
            not self.request.user.is_authenticated
            or self.request.user.profile.user_type == "Customer"
        ):
            return ["home/customerHome.html"]
        else:
            return ["home/workerHome.html"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profiles"] = Profile.objects.filter(user_type="Customer")
        return context


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


@login_required
def insurance(request):
    if request.method == "POST":
        i_form = InsuranceUpdateForm(request.POST, instance=request.user.insurance)
        if i_form.is_valid():
            i_form.save()
            messages.success(request, "Insurance information updated successfully.")
            return redirect("insurance")
        else:
            messages.error(
                request, "Error updating insurance information. Please check the form."
            )
    else:
        i_form = InsuranceUpdateForm(instance=request.user.insurance)
    context = {"i_form": i_form}
    return render(request, "home/insure.html", context)


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
