from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import *
from api.serializers import *
from rest_framework.permissions import IsAdminUser
from rest_framework import generics

@api_view(['GET'])
def routes(request):
    routes = {
        "Employees": "localhost/api/employees/",
        "customers" : "localhost/api/customers/",
        "products" : "localhost/api/products/"

    }
    return Response(routes)

# perform crud on customers if yor are employee member ->
class ProductListCreate( generics.ListAPIView, generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAdminUser]

class ProductDetailsUpdateDestroy( generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAdminUser]
    lookup_field = 'pk'

# perform crud on customers if yor are employee member ->
class CustomerListCreate(generics.ListCreateAPIView, generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes = [IsAdminUser]

class CustomerDetailsUpdateDestroy( generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAdminUser]
    lookup_field = 'pk'


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # permission_classes = [IsAdminUser]