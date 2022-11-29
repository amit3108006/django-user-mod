from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth.views import auth_login, auth_logout
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request=request, template_name="panel/dashboard.html")

def login(request):
    login_form = LoginForm(request.POST or None)
    if(login_form.is_valid()):
        #authenticate users
        user = authenticate(request, email=request.POST.get("email"), password=request.POST.get('password'))
        if user:
            auth_login(request, user)
            return redirect("/user/dashboard")
        #set the session and send user to dashboard
        #implement the validations as well
        #read about forms
        else:
            messages.error(request, "Invalid credentials, please check your email and password")

    context = {
        "form" : login_form
    }
    return render(request=request, template_name="user/login.html", context=context)

def forgotPassword(request):
    return render(request=request, template_name="user/forget-password.html")

def resetPassword(request):
    return render(request=request, template_name="user/reset-password.html")

def signup(request):
    return render(request=request, template_name="user/signup.html")


def dashboard(request):
    return render(request=request, template_name="panel/dashboard.html")