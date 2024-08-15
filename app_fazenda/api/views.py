from ..serializers import Farm, FarmSerializer
from rest_framework import generics

class FarmView(generics.CreateAPIView):
    model = Farm
    serializer_class = FarmSerializer
