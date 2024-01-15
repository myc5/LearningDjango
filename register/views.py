from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm

from .forms import RegisterForm


def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
            print("User saved")
    else:
        form = UserCreationForm()        
    return render(response, "register/register.html", {"form":form})

def register_custom(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            print("User saved")
        return redirect("/")
    else:
        form = RegisterForm()        
    return render(response, "register/register2.html", {"form":form})