from django.db import models


# Create your models here.
class Employee(models.Model):
    # name, email, dob, salary, disabled
    name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    dob = models.DateField(null=True)
    salary = models.DecimalField(max_digits=7, decimal_places=2)  # 67000.58
    disabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name
# python manage.py makemigrations
# python manage.py migrate
