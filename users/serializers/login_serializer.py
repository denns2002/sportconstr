from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=68, write_only=True)

    class Meta:
        model = get_user_model()
        fields = ["username", 'email', "password"]

    def validate(self, attrs):
        user_obj = (
            get_user_model().objects.filter(email=attrs.get("username")).first()
            or get_user_model().objects.filter(username=attrs.get("username")).first()
        )
        credentials = {"username": "", "password": attrs.get("password")}

        if user_obj:
            credentials["username"] = user_obj.username

        user = authenticate(username=credentials["username"], password=credentials["password"])
        if not user:
            raise AuthenticationFailed("Invalid credentials, try again.")
        if not user.is_active:
            raise AuthenticationFailed("Account disabled, contact admin.")
        attrs['user'] = user

        return attrs
