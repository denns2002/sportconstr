from django.contrib.auth import get_user_model
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from rest_framework import generics, status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from mailings.utils.send_email import send_token
from users.serializers.change_email_serializer import ChangeEmailSerializer
from users.utils.token import account_activation_token


class ChangeEmailAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChangeEmailSerializer

    def post(self, request):
        """Change email"""
        email = request.data.get("email")
        user = request.user

        if get_user_model().objects.filter(email=email):
            return Response(
                {'EROOR': "Email is used"}, status=status.HTTP_400_BAD_REQUEST)

        subject = 'Change email'
        body = "Hi, " + user.username + \
               "!\nUse link to change your email. If it's not your" \
               "response, change password or write in support!\n\n"
        params = f"&email={request.data['email']}"
        send_token(request, "email-verify-new", subject, body, user, email=email, params=params, is_change_email=True)

        return Response({'OK': "Check your new email"}, status=status.HTTP_200_OK)


@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def activate_new_email(request):
    User = get_user_model()
    uidb64 = request.GET.get('uidb64')
    token = request.GET.get('token')
    email = request.GET.get('email')

    try:
        uidb64 = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uidb64)

        if account_activation_token.check_token(user, token):
            user.email = email
            user.save()

            return Response(
                {"OK": "Successfully changed"},
                status=status.HTTP_200_OK
                )

    except Exception:
        pass

    return Response(
        {"OK": "Change link is invalid!"},
        status=status.HTTP_400_BAD_REQUEST
    )



