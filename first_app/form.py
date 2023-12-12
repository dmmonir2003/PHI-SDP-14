from django import forms
from first_app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields='__all__'
        lebels={
            'name':"student Name",
            'roll':"student Roll"
        }
        widgets={
            'name':forms.TextInput(attrs={'class':'btn-primary'})
        }
        help_texts={
            'father_name':'Write your father full name'
        }
        error_messages={
            'name':{'required':"your name is required"}
        }