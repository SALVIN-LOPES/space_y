
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('routes/', views.routes, name = 'routes'),

    path('products/', views.ProductListCreate.as_view(), name = 'producst_list_create'),
    path('products/<int:pk>/', views.ProductDetailsUpdateDestroy.as_view(), name = 'producst_detail_update_delete'),

    path('customers/', views.CustomerListCreate.as_view(), name = 'customer_list_create'),
    path('customers/<int:pk>/', views.CustomerDetailsUpdateDestroy.as_view(), name = 'customer_detail_update_delete'),

    # path('customers/', views.CustomerList.as_view(), name = 'customers'),
    path('employees/', views.EmployeeList.as_view(), name = 'employees'),
]
