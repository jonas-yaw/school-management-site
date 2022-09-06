from django.urls import path 
from .views import receipts_list_and_create,fees_catalogue_list_and_create,FeesCatalogueUpdateView,FeesCatalogueDeleteView

urlpatterns = [
    path('receipts/',receipts_list_and_create,name='receipts'),
    path('fees/',fees_catalogue_list_and_create,name='fees_catalogue'),
    path('dashboard/fees/<int:pk>/edit',FeesCatalogueUpdateView.as_view(),name='fees_catalogue_edit'),
    path('dashboard/fees/<int:pk>/delete',FeesCatalogueDeleteView.as_view(),name='fees_catalogue_delete'),
]