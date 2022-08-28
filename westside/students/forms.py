from django import forms

from .models import Student 

class StudentCreationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    year = forms.CharField(max_length=5)
    course = forms.CharField(max_length=255)

    class Meta:
        model = Student
        fields = ('first_name','last_name','year','course')
        

class CsvImportForm(forms.Form):
    excel_upload = forms.FileField()
