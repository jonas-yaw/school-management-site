from django.contrib import admin
from .models import Student
from import_export.admin import ImportExportModelAdmin

admin.site.register(Student)