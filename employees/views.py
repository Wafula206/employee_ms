from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm

@login_required
def profile(request):
    try:
        employee = Employee.objects.get(email=request.user.email)
    except Employee.DoesNotExist:
        employee = None
    return render(request, 'profile.html', {'employee': employee})

def is_staff(user):
    return user.is_staff

@user_passes_test(is_staff)
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})

@user_passes_test(is_staff)
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employees/employee_form.html', {'form': form})

@user_passes_test(is_staff)
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/employee_form.html', {'form': form})

@user_passes_test(is_staff)
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employees/employee_confirm_delete.html', {'employee': employee})

def home(request):
    employee = None
    if request.user.is_authenticated:
        try:
            employee = Employee.objects.get(email=request.user.email)
        except Employee.DoesNotExist:
            employee = None
    return render(request, 'home.html', {'employee': employee})

def about(request):
    return render(request, 'about.html')