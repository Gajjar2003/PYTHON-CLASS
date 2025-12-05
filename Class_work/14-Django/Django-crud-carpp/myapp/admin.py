from django.contrib import admin
from myapp.models import *


class cardetals(admin.ModelAdmin):
    list_display = ('name','model','price')

admin.site.register(car,cardetals)


# Register your models here.
