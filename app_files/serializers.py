from rest_framework import serializers
from .models import SourceFiles, Map
from app_mapa.serializers import MapSerializer


class SourceFilesSerializer(serializers.ModelSerializer):
    map = MapSerializer(read_only=True)

    class Meta:
        model = SourceFiles
        fields = ['id', 'title', 'file', 'map', 'user', 'description', 'accessed', 'when_was_accessed', 'created_at', 'updated_at']
