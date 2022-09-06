from email.policy import default
from random import choices
from .models import Receipt,FeesCatalogue
from django import forms

fee_type_choices = [
    ('BUS','BUS'),
    ('School fees','School fees')
]

class ReceiptsForm(forms.ModelForm):
    student_id = forms.CharField(max_length=255)
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    student_class = forms.CharField(max_length=50)
    fee_type = forms.CharField(max_length=50)
    amount_paid = forms.FloatField()
    term = forms.CharField(max_length=5)
    academic_year = forms.CharField(max_length=20)

    class Meta:
        model = Receipt
        fields = ('student_id','first_name','last_name','student_class','fee_type','amount_paid','term','academic_year')



class FeesCatalogueForm(forms.ModelForm):
    student_class = forms.CharField(max_length=255)
    term = forms.CharField(max_length=255)
    academic_year = forms.CharField(max_length=255)
    total_fees = forms.CharField(max_length=50)
    fee_type = forms.CharField(max_length=50)


    class Meta:
        model = FeesCatalogue
        fields = ('student_class','term','academic_year','total_fees','fee_type')
