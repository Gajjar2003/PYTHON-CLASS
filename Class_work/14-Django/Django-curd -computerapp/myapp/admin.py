from django.contrib import admin
from myapp.models import *

class display(admin.ModelAdmin):
    list_display = ('name','email','type','model','years','qty','price','gst','online','rating')

admin.site.register(computer,display)

# Register your models here.
