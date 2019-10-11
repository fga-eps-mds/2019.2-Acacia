from django.contrib import admin
from .models import User, Profile

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'username',
    )

    search_fields = ('email',)

admin.site.register(User, UserAdmin)
admin.site.register(Profile)
