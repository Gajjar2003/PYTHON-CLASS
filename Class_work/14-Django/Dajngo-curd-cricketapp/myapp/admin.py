from django.contrib import admin
from myapp.models import * 

class display(admin.ModelAdmin):
    list_display = ('no','name','age','email','type','fromate','run','con','score','avg','four','six')


admin.site.register(cricket,display)

# Register your models here.
