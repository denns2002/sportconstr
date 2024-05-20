from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class ChangeEmailSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=get_user_model().objects.all())],
        required=False
    )

    class Meta:
        model = get_user_model()
        fields = ("email",)
