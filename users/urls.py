from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register/", views.register, name="Registration Page"),
    path("login/", auth_views.LoginView.as_view(template_name="user-template/login.html"), name="Login Page"),
    path("logout/", auth_views.LogoutView.as_view(template_name="user-template/logout.html"), name="Logout Page"),
    path("reset/", auth_views.PasswordResetView.as_view(template_name="user-template/password_reset.html"),
         name="password_reset"),
    path("reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="user-template/password_reset_done.html"),
         name="password_reset_done"),
    path("reset/confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="user-template/password_reset_confirm.html"),
         name="password_reset_confirm"),
    path("reset/complete/",
         auth_views.PasswordResetDoneView.as_view(template_name="user-template/password_reset_complete.html"),
         name="password_reset_complete"),
    path("profile/", views.profile, name="Profile Page"),
]