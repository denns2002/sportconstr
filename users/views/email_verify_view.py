from django.contrib.auth import get_user_model
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from users.utils.token import account_activation_token


@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def activate(request):
    User = get_user_model()
    uidb64 = request.GET.get('uidb64')
    token = request.GET.get('token')

    try:
        uidb64 = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uidb64)

        if user.is_verified:
            return Response(
                {"OK": "The account is already verified"},
                status=status.HTTP_200_OK
                )

        if account_activation_token.check_token(user, token):
            user.is_verified = True
            user.save()

            return Response(
                {"OK": "Successfully activated"},
                status=status.HTTP_200_OK
                )

    except Exception:
        pass

    return Response(
        {"OK": "Activation link is invalid!"},
        status=status.HTTP_400_BAD_REQUEST
    )



