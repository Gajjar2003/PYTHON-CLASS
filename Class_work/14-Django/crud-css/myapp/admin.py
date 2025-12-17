from django.contrib import admin
from myapp.models import *

class display(admin.ModelAdmin):
    list_display = ('name','price','qty')

admin.site.register(product,display)
admin.site.register(Category)


