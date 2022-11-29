from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index),
    path("login", views.login),
    path("signup", views.signup),
    path("forgot-password", views.forgotPassword),
    path("reset-password", views.resetPassword),
    path("dashboard", views.dashboard)
]