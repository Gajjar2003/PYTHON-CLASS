from django.contrib import admin
from myapp.models import *

class display(admin.ModelAdmin):
    list_display = ('name','email','age','salary','dept')

admin.site.register(employee,display)
# Register your models here.
