from django.shortcuts import render
from.models import Student
from .forms import StudentForm

# Create your views here.
def login(request):
    return render(request,"login.html")

def login_list(request):
    student=Student.objects.all()
    return render(request,'login.html',{'student':student})

def student_form(request):
    form = StudentForm()

    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            age = form.cleaned_data["age"]

            return render(
                request,
                "success.html",
                {"name": name}
            )

    return render(request, "student_form.html", {"form": form})    