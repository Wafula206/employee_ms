from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('employees.urls')),  # This line is required for the home page to work!
    path('accounts/', include('django.contrib.auth.urls')),
]
