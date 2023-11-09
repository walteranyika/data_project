import os.path
import uuid

from django.db import models


def unique_img_name(instance, filename):
    name = uuid.uuid4()
    print(name)
    ext = filename.split(".")[-1]
    full_name = f"{name}.{ext}"
    # full_name = "%s.%s" % (name, ext)
    return os.path.join('employees', full_name)


# Create your models here.
class Employee(models.Model):
    # name, email, dob, salary, disabled
    name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    dob = models.DateField(null=True)
    salary = models.DecimalField(max_digits=7, decimal_places=2)  # 67000.58
    disabled = models.BooleanField(default=False)
    profile = models.ImageField(upload_to=unique_img_name, null=True, default="employees/employee.png")
    created_at = models.DateTimeField(auto_now_add=True, null=True)  # Once during creation
    updated_at = models.DateTimeField(auto_now=True, null=True)  # Every time an update happens

    def __str__(self):
        return self.name


COLORS = [
    ("Black", "Black"),
    ("Blue", "Blue"),
    ("White", "White"),
    ("Orange", "Orange"),
    ("Other", "Other"),
]


# https://vegibit.com/how-to-get-related-objects-in-django/
class Car(models.Model):
    employee = models.ForeignKey(Employee, related_name="employee", on_delete=models.CASCADE)
    plate = models.CharField(max_length=20, unique=True)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=60, choices=COLORS, default="White")

    def __str__(self):
        return f"{self.plate}, {self.make}"

# python manage.py makemigrations
# python manage.py migrate
# python manage.py populate

# pip install Pillow

# module package library
