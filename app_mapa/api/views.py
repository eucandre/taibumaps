from ..serializers import Map, MapSerializer
from rest_framework import viewsets

class MapView(viewsets.ModelViewSet):
    queryset = Map.objects.all()
    serializer_class = MapSerializer
    http_method_names = ['get']
