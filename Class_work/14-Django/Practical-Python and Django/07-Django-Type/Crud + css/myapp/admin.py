from django.contrib import admin
from myapp .models import *

class employeeshow(admin.ModelAdmin):
    list_display = ('name','email','age','salary','dept','address')

admin.site.register(Employee,employeeshow)
# Register your models here.
