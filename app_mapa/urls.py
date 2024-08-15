from django.urls import path
from .views import new, index, show
from .api.views import MapView

app_name = 'map'


urlpatterns = [
    path('', index, name='map_index'),
    path('new/', new, name='map_new'),
    path('show/<int:id>', show, name='map_show'),
    path('api/', MapView.as_view({'get':'list'}), name='map_api'),
]
