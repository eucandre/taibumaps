from rest_framework import serializers
from .models import Farm


class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = ('id', 'name','user','lat','long','created_at','updated_at')
        

    