from django.contrib import admin
from myapp.models import *

class studentadmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','email','age')
    search_fields= ('first_name', 'last_name','email','age')




admin.site.register(student,studentadmin)
admin.site.register(employee)

# Register your models here.
