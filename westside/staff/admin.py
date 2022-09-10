from django.contrib import admin
from .models import Staff
from import_export.admin import ExportActionMixin

class StaffAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = (
    'staff_id',
    'first_name',
    'last_name',
    )

admin.site.register(Staff,StaffAdmin)