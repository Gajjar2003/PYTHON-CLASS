from django.contrib import admin
from myapp.models import *

class display(admin.ModelAdmin):
    list_display = ('name','model','qty','price','gst','online')

# Register your models here.
admin.site.register(product,display)