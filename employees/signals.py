from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Employee
from django.utils import timezone

@receiver(post_save, sender=User)
def create_employee_profile(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:  # Only auto-create for regular users
        Employee.objects.create(
            user=instance,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email,
            hire_date=timezone.now().date(),
            gender='M',      # Default or make nullable in model
            phone='N/A',     # Default or make nullable in model
            status='Active'
        )

@receiver(post_save, sender=User)
def save_employee_profile(sender, instance, **kwargs):
    try:
        employee = Employee.objects.get(user=instance)
        employee.first_name = instance.first_name
        employee.last_name = instance.last_name
        employee.email = instance.email
        employee.save()
    except Employee.DoesNotExist:
        pass