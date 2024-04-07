
from django.contrib import admin
from django.urls import path, include
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('routes/', views.routes, name = 'routes'),

    path('users/', views.UserListCreate.as_view(), name = 'users_list_create'),
    path('users/<int:pk>/', views.UserDetailsUpdateDestroy.as_view(), name = 'users_detail_update_delete'),

    path('products/', views.ProductListCreate.as_view(), name = 'producst_list_create'),
    path('products/<int:pk>/', views.ProductDetailsUpdateDestroy.as_view(), name = 'producst_detail_update_delete'),

    path('customers/', views.CustomerListCreate.as_view(), name = 'customer_list_create'),
    path('customers/<int:pk>/', views.CustomerDetailsUpdateDestroy.as_view(), name = 'customer_detail_update_delete'),

    # path('customers/', views.CustomerList.as_view(), name = 'customers'),
    path('employees/', views.EmployeeListCreate.as_view(), name = 'employees_list_create'),
    path('employees/', views.EmployeeDetailsUpdateDestroy.as_view(), name = 'employees_detail_update_delete'),

    # user authentication
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
