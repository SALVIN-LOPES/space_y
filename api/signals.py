from django.db.models.signals import pre_save, post_save
from api.models import User, Customer, Employee, Product
from django.dispatch import receiver

@receiver(post_save, sender=User)
def customer_create(sender, instance=None,created=False, **kwargs):
    if created and instance.is_customer == True:
        Customer.objects.create(user=instance)

@receiver(post_save, sender=User)
def employee_create(sender, instance=None,created=False, **kwargs):
    if created and instance.is_employee == True:
        Employee.objects.create(user=instance)