from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from accounts.account_forms import LoginForm


def login_user(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "accounts/login.html", {"form": form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, "You are logged in successfully")
                return redirect('home')
        messages.error(request, 'Invalid username or password')
        return render(request, "accounts/login.html", {'form': form})


def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect("login")
