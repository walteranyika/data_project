from django.shortcuts import render, redirect

from main_app.app_forms import EmployeeForm


# Create your views here.
def home(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            for error, values in form.errors.items():
                print(error, values)
    else:
        form = EmployeeForm()
    return render(request, "employee.html", {"form": form})
