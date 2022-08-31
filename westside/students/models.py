from statistics import mode
from django.db import models
from django.urls import reverse

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    student_class = models.CharField(max_length=5, blank=True)
    date_of_birth = models.DateField()
    mother_name = models.CharField(max_length=255, blank=True)
    mother_contact = models.CharField(max_length=255, blank=True)
    father_name = models.CharField(max_length=255, blank=True)
    father_contact = models.CharField(max_length=255, blank=True)
    date_enrolled = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.first_name 


    def get_absolute_url(self): 
        return reverse('students')

