"""
URL configuration for data_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from data_project import settings
from main_app import views

urlpatterns = [
    path('', views.home, name="home"),
    path('employees', views.all_employees, name="all"),
    path('search', views.search_employees, name="search"),
    path('employees/<int:emp_id>', views.employee_details, name="details"),
    path('employees/delete/<int:emp_id>', views.employee_delete, name="delete"),
    path('employees/update/<int:emp_id>', views.employee_update, name="update"),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.accounts_url'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# "employees/<int:emp_id>"
# tables
# user
# admin , admin@gmail.com , 123456

# python manage.py migrate
# python manage.py createsuperuser
