from django.shortcuts import render, HttpResponse, redirect
from user.forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            new_user = User(username=username)
            new_user.set_password(password)
            new_user.save()

            messages.success(request, 'Successfully Registered')
            login(request, new_user)

            return redirect("index")
        else:
            context = {
                "form": form
            }
            return render(request, "register.html", context)

    else:
        form = RegisterForm()
        context = {
            "form": form
        }
        return render(request, "register.html", context)


def loginUser(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            messages.success(request, 'Successfully Logged in')

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect("index")
        else:
            context = {
                "form": form
            }
            return render(request, "login.html", context)

    else:
        form = LoginForm()
        context = {
            "form": form
        }
        return render(request, "login.html", context)


def logOut(request):
    logout(request)
    messages.success(request, "Logged out")
    return redirect("user:login")
