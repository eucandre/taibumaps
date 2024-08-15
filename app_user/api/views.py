# app_user/views.py

from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from ..serializers import UserSerializer

User = get_user_model()

class CreateUserView(generics.CreateAPIView):
    model = User
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
