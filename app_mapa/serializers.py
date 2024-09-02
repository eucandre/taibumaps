from rest_framework import serializers
from .models import Map
from app_fazenda.serializers import FarmSerializer


class MapSerializer(serializers.HyperlinkedModelSerializer):
    farm = FarmSerializer(read_only=True)
    

    class Meta:
        model = Map
        fields = ('id', 'name','lat', 'long', 'farm', 'url','description','main_map_selected','created_at','updated_at')
        

    