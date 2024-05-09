from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    USER_TYPES = [
        ("customer", "Customer"),
        ("worker", "Worker"),
        ("owner", "Owner"),
        ("supplier", "Supplier"),
    ]
    user_type = forms.ChoiceField(choices=USER_TYPES)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "user_type"]
