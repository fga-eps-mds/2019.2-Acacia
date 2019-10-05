from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'phone_number',
        'birth', 
        'email',
        'username',
    )

    search_fields = ('email',)

admin.site.register(User, UserAdmin)