# app_user/urls.py

from django.urls import path
from .api.views import CreateUserView, LoginAPI
from .views import register

urlpatterns = [
    path('register/', register, name='register'),
    path('api/login/', LoginAPI.as_view(), name='api-login'),
]
