from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from mailings.models import Mailing
from users.models import User
from users.utils.token import account_activation_token


def send_email(email_subject: str,
               email_body: str,
               to_emails: list | tuple,
               **boolean_fields) -> None:
    """
    Sends an email to a list of users. All mailings are stored in the database.

    :param str email_subject: message subject
    :param str email_body: message body
    :param str to_emails: recipients
    """
    from_email = settings.EMAIL_HOST_USER + settings.EMAIL_DOMAIN
    instance = Mailing.objects.create(
        subject=email_subject,
        body=email_body,
        from_email=from_email,
        **boolean_fields,
    )

    try:
        email = EmailMessage(
            subject=email_subject,
            body=email_body,
            to=to_emails,
            from_email=from_email,
        )
        email.send()

    except Exception as error:
        instance.is_error = True
        instance.error = error

    users = get_user_model().objects.filter(email__in=to_emails)
    for user in users:
        instance.to_emails.add(user)


def send_token(request, reverse_name, subject, body, user: User = None,
               email=None, params=None, **kwargs):
    token = account_activation_token.make_token(user)
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    domain = get_current_site(request).domain
    relative_link = reverse(reverse_name)
    params = params if params else ""
    url = f"http://{domain}{relative_link}?token={token}&uidb64={uidb64}" + params

    body += url
    if email:
        email = email
    elif user:
        email = user.email

    send_email(subject, body, [email], **kwargs)
