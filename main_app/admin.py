from django.contrib import admin

from main_app.models import Employee

# Register your models here.
admin.site.site_header = "Wezesha System"
admin.site.index_title = "Wezesha"


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "dob", "disabled"]
    search_fields = ["name", "email"]
    list_filter = ["disabled"]
    list_per_page = 25


admin.site.register(Employee, EmployeeAdmin)
