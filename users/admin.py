from django.contrib import admin
from django.contrib.auth import get_user_model


@admin.register(get_user_model())
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "created_at", "updated_at"]
    search_fields = [
        "username",
        "email",
        "first_name",
        "last_name",
    ]
    list_filter = ["created_at", "updated_at"]
    fields = [
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
        "is_verified",
        "created_at",
        "updated_at",
    ]
    readonly_fields = ["id", "created_at", "updated_at"]
