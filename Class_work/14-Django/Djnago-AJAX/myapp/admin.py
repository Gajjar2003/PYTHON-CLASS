from django.contrib import admin
from myapp.models import *

# Register your models here.
admin.site.register(product)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)