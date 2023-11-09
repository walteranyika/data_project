from django.contrib import admin

from main_app.models import Employee, Car

# Register your models here.
admin.site.site_header = "Wezesha System"
admin.site.index_title = "Wezesha"


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "dob", "disabled"]
    search_fields = ["name", "email"]
    list_filter = ["disabled"]


class CarAdmin(admin.ModelAdmin):
    list_display = ["employee", "make", "model", "plate"]


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Car, CarAdmin)
