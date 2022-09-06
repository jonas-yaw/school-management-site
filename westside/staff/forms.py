from django import forms
from .models import Staff 

class DateInput(forms.DateInput):
    input_type = 'date'

class StaffCreationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255,)
    role = forms.CharField(max_length=50)
    department = forms.CharField(max_length=200)
    date_of_birth = forms.DateField(widget=DateInput)
    staff_contact = forms.CharField(max_length=255)
    place_of_residence = forms.CharField(max_length=255)
    ssnit_number = forms.CharField(max_length=255)


    class Meta:
        model = Staff
        fields = ('first_name','last_name','role','department','date_of_birth',
        'staff_contact','place_of_residence','ssnit_number')


class CsvImportForm(forms.Form):
    excel_upload = forms.FileField()
