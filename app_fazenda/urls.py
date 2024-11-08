# app_user/urls.py

from django.urls import path
from .views import new, index, show, edit
from .api.views import FarmView, FarmViewSet
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('new/', login_required(new), name='farm_new'),
    path('', login_required(index), name='farm_index'),
    path('show/<int:id>', login_required(show), name='farm_show'),
    path('edit/<int:id>', login_required(edit), name='farm_edit'),
    path('api/', FarmView.as_view(), name='farm_api'),
    path('api/farm/', FarmViewSet.as_view({'get': 'list'}), name='farm_api'),
    path('api/farm/<int:id>', FarmViewSet.as_view({'get': 'retrieve'}), name='api-farm-detail'),
]
