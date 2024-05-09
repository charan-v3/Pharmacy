from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    USER_TYPES = [
        ("Customer", "Customer"),
        ("Worker", "Worker"),
        ("Owner", "Owner"),
        ("Admin", "Admin"),
    ]
    user_type = forms.ChoiceField(choices=USER_TYPES)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "user_type"]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    USER_TYPES = [
        ("Customer", "Customer"),
        ("Worker", "Worker"),
        ("Owner", "Owner"),
        ("Admin", "Admin"),
    ]
    user_type = forms.ChoiceField(choices=USER_TYPES)

    class Meta:
        model = User
        fields = ["username", "email", "user_type"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "image",
            "displayName",
            "Date_of_Birth",
            "bloodGroup",
            "phone",
            "TempAddress",
            "PermanentAddress",
        ]
