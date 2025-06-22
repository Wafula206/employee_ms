from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Position(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Employee(models.Model):
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
    def __str__(self):
        return f"{self.first_name} {self.last_name}"