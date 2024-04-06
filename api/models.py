from django.db import models
from django.contrib.auth.models import AbstractUser
# from api.serializers import UserSerializer
# -- > 20022001@Sc


# Create your models here.
class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    # first_name = models.CharField(max_length=100, null=True, blank=True) 
    # last_name = models.CharField(max_length=100, null=True, blank=True)


class Product(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    # image = models.ImageField(null=True, blank=True, default='/placeholder.jpg')
    brand = models.CharField(max_length=200, null=True, blank=True)
    category =models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank =True)
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank =True, default=0)
    price = models.IntegerField(null=True, blank =True, default=0)
    countInStock = models.IntegerField(null=True, blank =True, default=0 )
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

class Customer(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    bill = models.IntegerField(default=0, null=True)

    def __str__(self):
        return str(self.user.username)

class Employee(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    designation = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.user.username)