from django.urls import path
from .views import new, index, edit, delete

urlpatterns = [
    path('new/', new, name='new'),
    path('', index, name='index'),
    path('edit/<int:id>/', edit, name='edit'),
    path('delete/<int:id>/', delete, name='delete'),
]