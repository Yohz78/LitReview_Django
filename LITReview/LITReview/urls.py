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
    path("reviews/user-content", reviews.views.user_content, name="user-content"),
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
    path("reviews/create-ticket", reviews.views.ticket_upload, name="create-ticket"),
    path("reviews/<int:ticket_id>/edit", reviews.views.edit_ticket, name="edit-ticket"),
    path(
        "reviews/<int:id>/delete-follow",
        reviews.views.delete_follow,
        name="delete-follow",
    ),
    path(
        "reviews/<int:ticket_id>/create-review",
        reviews.views.review_upload,
        name="create-review",
    ),
    path("reviews/follow-user", reviews.views.follow_user, name="follow-user"),
    path(
        "reviews/create-reviewticket",
        reviews.views.create_reviewticket,
        name="create-reviewticket",
    ),
    path(
        "reviews/<int:review_id>/edit-review",
        reviews.views.edit_review,
        name="edit-review",
    ),
]
