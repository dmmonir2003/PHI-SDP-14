from django.shortcuts import render,redirect
from first_app.form import StudentForm

from . import models
# Create your views here.


def home(request):
    student=models.Student.objects.all()
    return render(request,'home.html',{'data':student})

def deletestudent(request,roll):
    models.Student.objects.get(pk=roll).delete()
    return redirect('homepage')

def studentForm(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form=StudentForm()
    return render(request,'form.html',{'form':form})
