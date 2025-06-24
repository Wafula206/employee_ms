from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Position(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15)
    hire_date = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, default='Active')
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Payroll(models.Model):
    PAYMENT_MODES = [
        ('phone', 'Phone (Mobile Money)'),
        ('bank', 'Bank Transfer'),
        ('cash', 'Cash'),
    ]
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    pay_period_start = models.DateField()
    pay_period_end = models.DateField()
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    allowances = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    net_pay = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    mode = models.CharField(max_length=10, choices=PAYMENT_MODES, default='phone')
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    date_processed = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('employee', 'pay_period_start', 'pay_period_end')

    def save(self, *args, **kwargs):
        self.net_pay = self.basic_salary + self.allowances - self.deductions
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee} - {self.pay_period_start} to {self.pay_period_end}"