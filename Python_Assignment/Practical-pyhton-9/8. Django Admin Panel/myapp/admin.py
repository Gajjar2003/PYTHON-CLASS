from django.contrib import admin
from .models import Doctor

class DoctorAdmin(admin.ModelAdmin):
    
    # Columns displayed in admin table
    list_display = ('name', 'specialization', 'hospital', 'experience', 'phone')

    # Search bar fields
    search_fields = ('name', 'specialization', 'hospital')

    # Filter options on right side
    list_filter = ('specialization', 'hospital')

    # Records per page
    list_per_page = 10

admin.site.register(Doctor, DoctorAdmin)