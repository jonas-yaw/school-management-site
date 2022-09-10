from django.contrib import admin
from .models import Student
from import_export.admin import ExportActionMixin

class StudentAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = (
    'student_id',
    'first_name',
    'last_name',
    )

admin.site.register(Student,StudentAdmin)