from django.contrib import admin
from  myapp.models import *

class Employeeshow(admin.ModelAdmin):
    list_display = ('name','email','age','dept','salary','gender','language','phone','city','pincode','address')

admin.site.register(Employee,Employeeshow)