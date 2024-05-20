from django.contrib import admin

from mailings.models import Mailing


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    fields = ['subject', 'is_error', 'datetime', 'from_email',
              'to_emails', 'body', 'is_verification',
              'is_change_password', 'is_reset_password', 'is_change_email']
    list_display = [
        'subject', 'is_error', 'from_email', 'datetime'
    ]
    list_filter = ['is_error',
                   'is_verification',
                   'is_change_password',
                   'is_reset_password',
                   'is_change_email']
    search_fields = [
        'subject', 'from_email', 'body', 'datetime'
    ]
    readonly_fields = fields
    filter_horizontal = ['to_emails']
