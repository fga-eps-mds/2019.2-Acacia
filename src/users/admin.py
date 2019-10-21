from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import User

class MyUserAdmin(UserAdmin):
    list_display = (
        'email',
        'username',
        'phone_number',
        'birth', 
    )

    # required fields to create a new user on SU admin page
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'username', 
                'password1', 
                'password2'
            ),
        }),
    )

    search_fields = ('email','username',)

admin.site.register(User, MyUserAdmin)