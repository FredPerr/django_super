from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['username', 'email']}),
        ('Sensible information', {'fields': ['password'], 'classes': ['collapse']}),
        ('Permissions', {'fields': ['is_staff', 'is_admin', 'is_superuser', 'is_active'], 'classes': ['collapse']})
    ]
    list_filter = ['date_joined', 'last_login', 'is_superuser', 'is_admin', 'is_staff']
    search_fields = ['id', 'username', 'email']
    list_display = ('id', 'username', 'email', 'is_superuser', 'is_admin')


admin.site.register(User, UserAdmin)
