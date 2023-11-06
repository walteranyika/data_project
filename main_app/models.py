import os
import random

from django.db import models

GENDERS = [
    ("Male", "Male"),
    ("Female", "Female"),
]

TEAMS = [
    ("Manchester United", "Manchester United"),
    ("Arsenal", "Arsenal"),
    ("Chelsea", "Chelsea"),
    ("Newcastle", "Newcastle"),
]


# Create your models here.

def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (random.randint(1000, 1000000), random.randint(1000, 900000), ext)
    return os.path.join('uploads', filename)


class Employee(models.Model):
    # name, email, dob, salary, disabled
    name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    dob = models.DateField(null=True)
    salary = models.DecimalField(max_digits=7, decimal_places=2)  # 67000.58
    disabled = models.BooleanField(default=False)
    gender = models.CharField(max_length=20, default="Male", choices=GENDERS)
    profile = models.ImageField(upload_to=content_file_name, null=True)

    def __str__(self):
        return self.name
# python manage.py makemigrations
# python manage.py migrate
