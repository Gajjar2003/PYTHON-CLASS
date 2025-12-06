from django.contrib import admin
from myapp.models import *

class empdisplay(admin.ModelAdmin):
    list_display = ('name','email','age','salary','department')


admin.site.register(employee,empdisplay)

# Register your models here.
