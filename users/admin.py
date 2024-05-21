from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


@admin.register(get_user_model())
class UserAdmin(UserAdmin):
    list_display = ["username", "email", "created_at", "updated_at"]
    search_fields = [
        "username",
        "email",
        "first_name",
        "last_name",
    ]
    list_filter = ["created_at", "updated_at"]

    fieldsets = (
        (None, {'fields': ('id', 'username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', "is_verified", 'groups','user_permissions')}),
        ('Important dates', {'fields': ('created_at', 'updated_at')}),
    )

    readonly_fields = ["id", "created_at", "updated_at"]
