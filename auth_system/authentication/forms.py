# IMPORT Required MODULES
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


# Login form definition
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Additional field for email

    class Meta:
        model = User  # Use the custom User model
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]  # Include fields for registration
