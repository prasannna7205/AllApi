from django.contrib import admin
from viewapp.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','eno','ename','esal','eddrs']

admin.site.register(Employee,EmployeeAdmin)