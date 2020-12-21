from django.contrib import admin
from testapp.models import Employee

# Register your models here.
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display=['id','empname','empsalary']

admin.site.register(Employee,EmployeeModelAdmin)
