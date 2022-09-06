from django.urls import path 
from .views import *

urlpatterns = [
    path('dashboard/staff',staff_list_and_create,name='staff'),
    path('dashboard/staff/<int:pk>/edit',StaffUpdateView.as_view(),name='staff_edit'),
    path('dashboard/staff/<int:pk>/delete',StaffDeleteView.as_view(),name='staff_delete'),
]