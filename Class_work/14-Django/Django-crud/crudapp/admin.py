from django.contrib import admin
from crudapp.models import *

# Register your models here.
class studentadmin(admin.ModelAdmin):
    list_display = ('name', 'email','age')

admin.site.register(student,studentadmin)