from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "accounts/signup.html", {
        "form": form
    })

    

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "accounts/login.html")


    

@login_required(login_url="login")
def dashboard(request):
    return render(request, "accounts/dashboard.html")




def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")

    return redirect("dashboard")


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'home.html')

def contact2(request):
    return render(request, 'home.html')    
    
def signup(request):
    return render(request, 'accounts/signup.html')
    