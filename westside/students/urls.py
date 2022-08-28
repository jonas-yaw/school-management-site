from django.urls import path 
from .views import *

urlpatterns = [
    path('dashboard/',DashboardView.as_view(),name='dashboard'),
    path('dashboard/students',list_and_create,name='students'),
    path('dashboard/students/<int:pk>/edit',StudentUpdateView.as_view(),name='student_edit'),
    path('dashboard/students/<int:pk>/delete',StudentDeleteView.as_view(),name='student_delete'),
    path('dashboard/students/import',simple_upload,name='upload_csv'),
]