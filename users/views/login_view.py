from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from users.serializers.login_serializer import LoginSerializer

from mailings.utils.send_email import send_token


class LoginAPIView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        """
        Login.
        """
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        user = get_user_model().objects.get(username=serializer.data["username"])

        if not user.is_verified:
            subject = 'Verify your email'
            body = "Hi, " + user.username + \
                   "!\nUse link to verify your email. \n\n"
            send_token(request, "email-verify", subject, body, user, is_verification=True)

            return Response(
                {"OK": f"Hello, {user}! We sent you a confirmation email"},
                status=status.HTTP_200_OK,
            )

        return Response(serializer.data, status=status.HTTP_200_OK)
