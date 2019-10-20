from django.urls import path
from django.views.generic import TemplateView

from .views import login

urlpatterns = [
    path('', login, name="login"),
]
