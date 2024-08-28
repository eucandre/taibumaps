from ..serializers import Farm, FarmSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated



class FarmView(generics.CreateAPIView):
    model = Farm
    serializer_class = FarmSerializer

class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    permission_classes = [IsAuthenticated]