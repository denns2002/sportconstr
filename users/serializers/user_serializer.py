from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "username",
            "email",
            "is_staff",
            "is_active",
            "is_verified",
            "first_name",
            "last_name",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id", "created_at", "updated_at", "is_staff",
            "is_active", "is_verified"
        ]
