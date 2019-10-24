from django.contrib import admin
from .models import Property


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        'owner',
        'type_of_address',
        'state',
        'BRZipCode',
        'city',
        'district',
    )

    list_filter = (
        'type_of_address',
        'state',
    )
