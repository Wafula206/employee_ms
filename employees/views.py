from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Payroll
from .forms import EmployeeForm, PayrollForm

def is_staff(user):
    return user.is_staff

# --- EMPLOYEE INTERFACES ---

@login_required
def profile(request):
    employee = None
    if request.user.is_authenticated:
        try:
            employee = Employee.objects.get(user=request.user)
        except Employee.DoesNotExist:
            employee = None
    return render(request, 'employees/profile.html', {'employee': employee})

@login_required
def employee_payroll_history(request):
    try:
        employee = Employee.objects.get(user=request.user)
        payrolls = Payroll.objects.filter(employee=employee).order_by('-pay_period_start')
    except Employee.DoesNotExist:
        payrolls = []
        employee = None
    return render(request, 'employees/employee_payroll_history.html', {'payrolls': payrolls, 'employee': employee})

# --- STAFF INTERFACES ---

@user_passes_test(is_staff)
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})

@user_passes_test(is_staff)
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
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
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
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

@user_passes_test(is_staff)
def payroll_list(request):
    payrolls = Payroll.objects.all().order_by('-pay_period_start')
    return render(request, 'employees/payroll_list.html', {'payrolls': payrolls})

@user_passes_test(is_staff)
def payroll_detail(request, pk):
    payroll = get_object_or_404(Payroll, pk=pk)
    return render(request, 'employees/payroll_detail.html', {'payroll': payroll})

@user_passes_test(is_staff)
def payroll_create(request):
    if request.method == 'POST':
        form = PayrollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payroll_list')
    else:
        form = PayrollForm()
    return render(request, 'employees/payroll_form.html', {'form': form})

@user_passes_test(is_staff)
def payroll_update(request, pk):
    payroll = get_object_or_404(Payroll, pk=pk)
    if request.method == 'POST':
        form = PayrollForm(request.POST, instance=payroll)
        if form.is_valid():
            form.save()
            return redirect('payroll_list')
    else:
        form = PayrollForm(instance=payroll)
    return render(request, 'employees/payroll_form.html', {'form': form})

@user_passes_test(is_staff)
def payroll_delete(request, pk):
    payroll = get_object_or_404(Payroll, pk=pk)
    if request.method == 'POST':
        payroll.delete()
        return redirect('payroll_list')
    return render(request, 'employees/payroll_confirm_delete.html', {'payroll': payroll})

def home(request):
    employee = None
    if request.user.is_authenticated:
        try:
            employee = Employee.objects.get(user=request.user)
        except Employee.DoesNotExist:
            employee = None
    return render(request, 'employees/home.html', {'employee': employee})

def about(request):
    return render(request, 'employees/about.html')