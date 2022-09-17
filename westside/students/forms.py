from django import forms

from .models import Student

class DateInput(forms.DateInput):
    input_type = 'date'

class StudentCreationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255,)
    student_class = forms.CharField(max_length=50)
    date_of_birth = forms.DateField(widget=DateInput)
    mother_name = forms.CharField(max_length=255)
    mother_contact = forms.CharField(max_length=255)
    father_name = forms.CharField(max_length=255)
    father_contact = forms.CharField(max_length=255)
    place_of_residence = forms.CharField(max_length=255)

    class Meta:
        model = Student
        fields = ('first_name','last_name','student_class','date_of_birth','mother_name',
        'mother_contact','father_name','father_contact','place_of_residence')
        

class CsvImportForm(forms.Form):
    excel_upload = forms.FileField()

class SearchForm(forms.Form):
    student_name = forms.CharField(max_length=255)
