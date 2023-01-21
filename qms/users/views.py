from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.http import HttpResponse
from django.contrib.auth.models import User

def register(request):
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get("username")
                messages.success(request, f'Account created for {username}!')
                return redirect("users-login")
        else:
            form = CustomUserCreationForm()
        return render(request, "users/register.html", {"form": form})


def profile(request, username):
    user = User.objects.get(username=username)
    context = {"user": user}
    return render(request, "users/profile.html", context=context)