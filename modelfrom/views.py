# Create your views here.
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import vipin

def student_create(request):

    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return render( request,'sccece.html')

    else:
        form = StudentForm()

    return render(request, 'student.html', {'form': form})

    

#read data
def student_list(request):

    students = vipin.objects.all()

    return render(request, 'data.html', { 'students': students })