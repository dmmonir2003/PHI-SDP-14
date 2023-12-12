
from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='homepage'),
    path('delete/<int:roll>',views.deletestudent,name='delete_student'),
    path('form/',views.studentForm,name='form')
]
