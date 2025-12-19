from django.contrib import admin
from myapp.models import *

class display(admin.ModelAdmin):
    list_display = ('name','email','age','phone')

admin.site.register(student,display)