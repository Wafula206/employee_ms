from django import forms
from .models import Employee, Payroll

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'hire_date': forms.DateInput(attrs={'type': 'date'})
        }

class PayrollForm(forms.ModelForm):
    class Meta:
        model = Payroll
        fields = '__all__'
        widgets = {
            'pay_period_start': forms.DateInput(attrs={'type': 'date'}),
            'pay_period_end': forms.DateInput(attrs={'type': 'date'}),
        }