from django.shortcuts import render, redirect
from django.contrib.auth import aauthenticate, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, SignupForm


# Handles user signup
def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = SignupForm()
    return render(request, "signup.html", {"form": form})


# Login view
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("profile")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


# Logout view
def logout_view(request):
    logout(request)
    return redirect("login")


# Profile view
@login_required
def profile_view(request):
    return render(request, "profile.html", {"user": request.user})
