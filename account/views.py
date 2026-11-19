from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Subject

def signup_view(request):

    if request.method == 'POST':

        form = SignupForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Registration successful!"
            )

            return redirect('login')

    else:
        form = SignupForm()

    return render(
        request,
        'box/singup.html',
        {'form': form}
    )

    #login
def login_view(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('home')

        else:
            messages.error(request, "Invalid username or password!")

    return render(request, 'box/login.html')

#dasbord
@login_required(login_url='login')
def dashboard(request):
    return render(request, 'box/dashbord.html')

#@login_required(login_url='login')
def dash(request):
    return render(request, 'about.html')

@login_required(login_url='login')
def home(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def contact(request):
    return render(request, 'home.html')

    

    
#logout
def logout_view(request):

    logout(request)

    messages.success(request, "You have logged out successfully!")

    return redirect('login')


def subject(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        pdf = request.FILES.get('pdf')
        code = request.POST.get('code')
        title = request.POST.get('title')

        Subject.objects.create(
            name=name,
            pdf=pdf,
            code=code,
            title=title
        )

        return redirect('subject')

    subjects = Subject.objects.all()

    return render(request, 'box/subject.html', {
        'subjects': subjects
    })

def subdata(request):
    subjects = Subject.objects.all()
    return render(request,'box/subdata.html',{
        'subjects':subjects
    })