from django.contrib import admin
from .models import FeesCatalogue,Receipt
from import_export.admin import ExportActionMixin

class ReceiptAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = (
    'student_id',
    'first_name',
    'last_name',
    )


class FeesCatalogueAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = (
    'student_class',
    'academic_year',
    'total_fees',
    )

admin.site.register(Receipt,ReceiptAdmin)
admin.site.register(FeesCatalogue,FeesCatalogueAdmin)
