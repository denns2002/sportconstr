from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.response import Response

from mailings.utils.send_email import send_token
from users.serializers.register_serializer import RegisterSerializer


class RegisterAPIView(generics.GenericAPIView):
    permission_classes = []
    serializer_class = RegisterSerializer

    def post(self, request):
        """Register and send email verify if the user is not verified."""

        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data  # {'username': 'string', 'email': 'user@example.com', 'is_verified': True}
        user = get_user_model().objects.get(email=user_data['email'])

        if not user.is_verified:
            subject = 'Verify your email'
            body = "Hi, " + user.username + \
                   "!\nUse link to verify your email. \n\n"
            send_token(request, "email-verify", subject, body, user, is_verification=True)

        return Response(user_data, status=status.HTTP_201_CREATED)
