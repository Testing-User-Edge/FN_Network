from django.shortcuts import render, redirect
from .form import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Your account has been created successfully! You are not able to login to the website.")
            return redirect("Login Page")
    else:
        form = UserRegistrationForm()
    return render(request, "user-template/register.html", {"form" : form, "title": "Register"})

@login_required
def profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            messages.success(request, f"Your account has been updated successfully!")
            return redirect("Profile Page")
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
        "title": "Profile"
    }
    return render(request, "user-template/profile.html", context)

