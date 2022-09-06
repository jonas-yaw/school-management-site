from statistics import mode
from django.db import models
from django.urls import reverse

class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=200, blank=True)
    date_of_birth = models.DateField()
    staff_contact = models.CharField(max_length=255, blank=True)
    place_of_residence = models.CharField(max_length=255, blank=True)
    ssnit_number = models.CharField(max_length=255, blank=True)
    date_employed = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.first_name 


    def get_absolute_url(self): 
        return reverse('staff')

    class Meta:
        ordering = ['-date_employed']


