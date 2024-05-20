from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        for field in (username, email, password):
            if field is None:
                raise TypeError(f"Users should have a {field.__class__.__name__}")

        user = self.model(
            username=username,
            email=self.normalize_email(email).lower(),
            **extra_fields,
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, password, **extra_fields):
        email = username + "@" + username + ".com"
        user = self.create_user(
            username,
            email,
            password,
            is_superuser=True,
            is_staff=True,
            is_verified=True,
        )
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=255,
        unique=True,
        db_index=True,
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
        db_index=True,
        blank=True,
        null=True,
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "username"

    def __str__(self):
        return f"{str(self.username)} {str(self.email)}"

    class Meta:
        verbose_name, verbose_name_plural = "User", "Users"
