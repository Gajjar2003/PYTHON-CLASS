from django.contrib import admin
from myapp.models import *

class studentshow(admin.ModelAdmin):
    list_display = ('name','age','email')

admin.site.register(Student,studentshow)




# Register your models here.
