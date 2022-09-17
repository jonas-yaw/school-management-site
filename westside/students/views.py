from email import message
from operator import index
from urllib.request import Request
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from django.shortcuts import render
from .forms import StudentCreationForm,CsvImportForm,SearchForm
from .models import Student
from django.urls import reverse_lazy

import pandas as pd 
from .resources import StudentResource
from django.contrib import messages
from django.http import HttpResponse
from tablib import Dataset

from django.db.models import Count
from users.models import CustomUser

from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from django.core.paginator import Paginator 
import datetime 


class DashboardView(TemplateView):
    template_name = 'dashboard.html'


def list_and_create(request):
    form = StudentCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()

    
    # notice this comes after saving the form to pick up new objects
    objects = Student.objects.all()

    p = Paginator(Student.objects.all(),10)
    page = request.GET.get('page')
    student_list = p.get_page(page)

    nums = "a" * student_list.paginator.num_pages

    search_form = SearchForm(request.GET or None)
    if request.method == 'GET' and search_form.is_valid():
        student_name = request.GET['student_name']
        print(student_name)

        searched_students = Student.objects.filter(first_name__icontains=student_name) | Student.objects.filter(last_name__icontains=student_name)

        pagn = Paginator(searched_students.all(),10)
        page1 = request.GET.get('page')
        searched_students_list = pagn.get_page(page1)

        numbs = "a" * searched_students_list.paginator.num_pages
        return render(request, 'student_list_search.html', {
        'searched_students': searched_students_list,
        'numbs':numbs
        })


    return render(request, 'student_list.html', {'objects': objects,
    'student_list':student_list,
    'nums':nums, 
    'form': form,
    'search_form':search_form
    })


def student_search(request):
    search_form = SearchForm(request.GET or None)
    if request.method == 'GET' and search_form.is_valid():
        student_name = request.GET['student_name']

        searched_students = Student.objects.filter(first_name__icontains=student_name) | Student.objects.filter(last_name__icontains=student_name)

        return render(request, 'student_list_search.html', {'searched_students': searched_students})



class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'student_update.html'
    fields = ['first_name','last_name',
    'student_class','date_of_birth','mother_name',
    'mother_contact','father_name','father_contact','place_of_residence']

    def dispatch(self, request, *args, **kwargs):
        if self.request.user != CustomUser.objects.get(username="admin"):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)



class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_delete.html'
    success_url = reverse_lazy('students')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user != CustomUser.objects.get(username="admin"):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)



def simple_upload(request):
    form = CsvImportForm(request.POST or None)

    info = '' 
    if request.method == 'POST':
        new_student = request.FILES['excel_upload']

        if not new_student.name.endswith('xlsx'):
            info = 'Wrong Format'
        else:
            imported_data = pd.read_excel(new_student)

            count = len(imported_data)-1


            for data in imported_data.index:
                new_record = imported_data.iloc[count].tolist()
                Student.objects.update_or_create(
                first_name = new_record[1],
                last_name = new_record[2],
                student_class = new_record[3],
                date_of_birth = new_record[4],
                mother_name = new_record[5],
                mother_contact = new_record[6],
                father_name = new_record[7],
                father_contact = new_record[8],
                place_of_residence = new_record[9],
                date_enrolled = new_record[4]
                )
                count = count - 1
                


    return render(request,'import_data.html',{'form': form,'info':info})




def Student_population(request):
    labels = []
    data = []

    querySet = Student.objects.values('student_class').annotate(class_population=Count('student_class')).order_by('-class_population')
    for x in querySet:
        labels.append(x['student_class'])
        data.append(x['class_population'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })