from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page at root
    path('about/', views.about, name='about'),

    # Staff: Employee management
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/create/', views.employee_create, name='employee_create'),
    path('employees/<int:pk>/edit/', views.employee_update, name='employee_update'),
    path('employees/<int:pk>/delete/', views.employee_delete, name='employee_delete'),

    # Employee: Profile and payroll history
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/profile/payroll/', views.employee_payroll_history, name='employee_payroll_history'),

    # Staff: Payroll management
    path('payrolls/', views.payroll_list, name='payroll_list'),
    path('payrolls/create/', views.payroll_create, name='payroll_create'),
    path('payrolls/<int:pk>/', views.payroll_detail, name='payroll_detail'),
    path('payrolls/<int:pk>/edit/', views.payroll_update, name='payroll_update'),
    path('payrolls/<int:pk>/delete/', views.payroll_delete, name='payroll_delete'),
]