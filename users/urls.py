from django.urls import path

from users.views.change_email_view import ChangeEmailAPIView, activate_new_email
from users.views.email_verify_view import activate
from users.views.login_view import LoginAPIView
from users.views.logout_view import Logout
from users.views.register_view import RegisterAPIView
from users.views.reset_password_view import (
    PasswordTokenCheckAPI,
    RequestPasswordResetAPIView, SetPasswordTokenAPI
)
from users.views.user_view import UserDetailAPIView, UserListAPIView

urlpatterns = [
    path("login/", LoginAPIView.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("email-verify/", activate, name="email-verify"),

    path("request-pass-reset/",
         RequestPasswordResetAPIView.as_view(),
         name="request-pass-reset"),
    path("password-token-check/<uidb64>/<token>/",  # GET PATCH
         PasswordTokenCheckAPI.as_view(),
         name="password-token-check"),
    path("set-password-token/", SetPasswordTokenAPI.as_view(), name="set-password-token"),

    path("change-email/", ChangeEmailAPIView.as_view(), name="change-email"),
    path("email-verify-new/", activate_new_email, name="email-verify-new"),

    path("user-list/", UserListAPIView.as_view(), name="user-list"),
    path("user-detail/<int:id>", UserDetailAPIView.as_view(), name="user-detail"),
]
