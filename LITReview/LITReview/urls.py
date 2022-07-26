from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordChangeDoneView,
    LoginView,
    LogoutView,
)
import authentification.views
import reviews.views


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "login/",
        LoginView.as_view(
            template_name="authentification/login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("home/", reviews.views.home, name="home"),
    path(
        "change-password/",
        PasswordChangeView.as_view(
            template_name="authentification/password_change.html"
        ),
        name="password_change",
    ),
    path(
        "change-password-done/",
        PasswordChangeDoneView.as_view(
            template_name="authentification/password_change_done.html"
        ),
        name="password_change_done",
    ),
    path("signup", authentification.views.signup_page, name="signup"),
]
