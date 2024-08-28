from django.urls import path
from .api.views import CreateUserView, LoginAPI, UserViewSet
from .views import register

urlpatterns = [
    path('register/', register, name='register'),
    path('api/login/', LoginAPI.as_view(), name='api-login'),
    path('', UserViewSet.as_view({'get': 'list'}), name='api-user-list'),  # Listar usuários
    path('<int:pk>/', UserViewSet.as_view({'get': 'retrieve'}), name='api-user-detail'),  # Obter detalhes de um usuário
]
