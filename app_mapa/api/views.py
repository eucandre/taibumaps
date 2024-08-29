from ..serializers import Map, MapSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class MapView(viewsets.ReadOnlyModelViewSet):
    queryset = Map.objects.all()
    serializer_class = MapSerializer
    http_method_names = ['get']
    #permission_classes = [IsAuthenticated]
