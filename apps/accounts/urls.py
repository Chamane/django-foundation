from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as authViews

from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('register', views.register, name="register"),
    path('logout', authViews.LogoutView.as_view(), name="logout"),
]
