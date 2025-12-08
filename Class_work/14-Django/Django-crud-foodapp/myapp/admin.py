from django.contrib import admin
from myapp.models import *

class display(admin.ModelAdmin):
    list_display = ('name','veg','qty','price','gst','rating')

admin.site.register(food,display)
