from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models


class Mailing(models.Model):
    is_verification = models.BooleanField(default=False)
    is_change_password = models.BooleanField(default=False)
    is_change_email = models.BooleanField(default=False)
    is_reset_password = models.BooleanField(default=False)
    is_error = models.BooleanField(default=False,)
    error = models.TextField(blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    to_emails = models.ManyToManyField(get_user_model())
    from_email = models.CharField(
        max_length=255,
        default=settings.EMAIL_HOST_USER + settings.EMAIL_DOMAIN,
        blank=True,
        null=True
    )
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name, verbose_name_plural = "Mailing", "Mailings"
