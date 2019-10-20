from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('register', views.register, name="register"),
]
