from rest_framework import serializers
from .models import Map


class MapSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Map
        fields = ('id', 'name', 'farm', 'url','description','main_map_selected','created_at','updated_at')
        

    