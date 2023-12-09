from django.shortcuts import render,redirect

from . import models
# Create your views here.


def home(request):
    student=models.Student.objects.all()
    return render(request,'home.html',{'data':student})

def deletestudent(request,roll):
    models.Student.objects.get(pk=roll).delete()
    return redirect('homepage')
