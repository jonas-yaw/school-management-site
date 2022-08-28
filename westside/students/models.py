from django.db import models
from django.urls import reverse

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    year = models.CharField(max_length=5, blank=True)
    course = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.first_name 


    def get_absolute_url(self): # new
        return reverse('students')