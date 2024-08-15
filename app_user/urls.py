# app_user/urls.py

from django.urls import path
from .api.views import CreateUserView
from .views import register

urlpatterns = [
    path('register/', register, name='register'),
]
