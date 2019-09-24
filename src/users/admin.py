from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'birth', 'phone_number', 'email')
    search_fields = ('email',)

admin.site.register(User, UserAdmin)