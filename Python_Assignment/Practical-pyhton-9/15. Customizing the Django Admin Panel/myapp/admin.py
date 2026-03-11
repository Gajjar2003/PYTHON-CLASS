from django.contrib import admin
from myapp.models import *

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):

    # Columns shown in admin list
    list_display = (
        'id',
        'name',
        'specialization',
        'experience',
        'availability',
        'consultation_fee'
    )

    # Search functionality
    search_fields = ('name', 'specialization')

    # Filter options
    list_filter = ('specialization', 'availability')

    # Sort data
    ordering = ('name',)

    # Editable fields directly in list
    list_editable = ('availability', 'consultation_fee')

    # Organize fields in admin form
    fieldsets = (
        ("Doctor Personal Info", {
            'fields': ('name', 'age', 'email', 'phone')
        }),

        ("Professional Details", {
            'fields': ('specialization', 'experience')
        }),

        ("Hospital Details", {
            'fields': ('availability', 'consultation_fee')
        }),
    )