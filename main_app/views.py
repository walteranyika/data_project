from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect

from main_app.app_forms import EmployeeForm
from main_app.models import Employee


# Create your views here.
def home(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = EmployeeForm()
    return render(request, "employee.html", {"form": form})


# Model View Template

# All employees
# One employee
def all_employees(request):
    # employees = Employee.objects.all().order_by("-dob")  # SELECT * FROM employees
    # employees = Employee.objects.filter(Q(name__istartswith='l') & Q(email__contains="k"))  # SELECT * FROM employees
    # employees = Employee.objects.filter(Q(name__istartswith='l') | Q(email__contains="k"))  # SELECT * FROM employees
    # employees = Employee.objects.filter(Q(name__istartswith='l') & ~Q(email__contains="k"))  # SELECT * FROM employees
    employees = Employee.objects.filter(Q(name__istartswith='l') & ~Q(email__contains="k")).values('name', 'id', 'email','dob', 'salary')  # SELECT * FROM employees
    paginator = Paginator(employees, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "all_employees.html", {"employees": page_obj})


def employee_details(request, emp_id):
    employee = Employee.objects.get(pk=emp_id)  # SELECT * FROM employees WHERE id=1
    return render(request, "employee_details.html", {"employee": employee})
