from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import *
from api.serializers import *
from rest_framework import generics
from api.permissions import IsEmployeeUser, IsCustomerUser
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication


# decode password -> 
from django.contrib.auth.hashers import make_password

@api_view(['GET'])
def routes(request):
    routes = {
        "routes" : "https://space-y-2q6d.onrender.com/api/routes/",

        # PRODUCTS (send token : only employees can create products)
            # GET - POST
        "products" : "https://space-y-2q6d.onrender.com/api/products/",
            # PUT - DELETE
        "products" : "https://space-y-2q6d.onrender.com/api/products/<int:pk>/",
        
        # CUSTOMERS 
            # GET - POST
        "customers" : "https://space-y-2q6d.onrender.com/api/customers/",
            # PUT - DELETE
        "customers" : "https://space-y-2q6d.onrender.com/api/customers/<int:pk>/",

        # EMPLOYEES (only isAdminUser can fetch employees)
            # GET - POST
        "employees" : "https://space-y-2q6d.onrender.com/api/employees/",
            # PUT - DELETE
        "employees" : "https://space-y-2q6d.onrender.com/api/employees/<int:pk>/",

        # USER (while creating user : define is_employee || is_customer && no bearer token)
            # GET - POST
        "users" : "https://space-y-2q6d.onrender.com/api/users/",
            # PUT - DELETE
        "users" : "https://space-y-2q6d.onrender.com/api/users/<int:pk>/",
    }
    return Response(routes)

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerWithToken
    # permission_classes = [IsEmployeeUser]

class UserDetailsUpdateDestroy( generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerWithToken
    # permission_classes = [IsAdminUser]
    lookup_field = 'pk'

# perform crud on customers if yor are employee member ->
class ProductListCreate( generics.ListAPIView, generics.CreateAPIView):
    # authentication_classes = (JWTAuthentication)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsEmployeeUser]

class ProductDetailsUpdateDestroy( generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsEmployeeUser]
    lookup_field = 'pk'

# perform crud on customers if yor are employee member ->
class CustomerListCreate(generics.ListCreateAPIView, generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsEmployeeUser]

class CustomerDetailsUpdateDestroy( generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsEmployeeUser]
    lookup_field = 'pk'


class EmployeeListCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminUser]

class EmployeeDetailsUpdateDestroy( generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'

class OrderListCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsCustomerUser]

class OrderDetailsUpdateDestroy( generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsCustomerUser]
    lookup_field = 'pk'