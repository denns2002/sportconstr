from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=get_user_model().objects.all())],
        required=False
    )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=get_user_model().objects.all())],
        required=True
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password_2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = get_user_model()
        fields = ("username", "email", "password", "password_2", "is_verified")

    def validate(self, attrs):
        if attrs["password"] != attrs["password_2"]:
            raise serializers.ValidationError(
                {"ERROR": "Password fields didn't match"}
            )

        return attrs

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            is_verified=validated_data["is_verified"]
        )
        Token.objects.create(user=user)
        user.set_password(validated_data["password"])
        user.save()

        return user
