from django.db import models
from students.models import Student 
from django.contrib.auth import get_user_model

from django.urls import reverse

class Receipts(models.Model):
    student_id = models.AutoField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    student_class = models.CharField(max_length=20)
    fee_type = models.CharField(max_length=20)
    balance = models.FloatField(max_length=255)
    academic_year = models.CharField(max_length=20)
    term = models.CharField(max_length=5)
    payment_date = models.DateField(auto_now_add=True)
    receipient =  models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.student_id 


    def get_absolute_url(self): 
        return reverse('students')

    class Meta:
        ordering = ['payment_date']

class FeesCatalogue(models.Model):
    student_class = models.CharField(max_length=5)
    term = models.CharField(max_length=5)
    academic_year = models.CharField(max_length=20)
    total_fees  = models.FloatField(max_length=255)
