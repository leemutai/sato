from django.contrib import admin

from main_app.models import Employee

admin.site.site_header = "Warezes System"
admin.site.index_title = "Warezes"


# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "dob", "disabled"]
    search_fields = ['name', "email"]
    list_filter = ['disabled']


admin.site.register(Employee, EmployeeAdmin)
